from django.db.models import Avg, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator


from .forms import RegistrationForm, EditUserForm
from .models import User, UserWorkOffice
from ratings.models import Review


@login_required
def search(request):
    queryset = User.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(title__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
    }
    return render(request, 'search.html', context)


@login_required
def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_review = Review.objects.filter(reviewed_user=user)
    avg_rating = Review.objects.filter(reviewed_user=user).aggregate(avg_professionalism=Avg('rate_professionalism'),
                                                                     avg_teamwork=Avg(
                                                                         'rate_teamwork'),
                                                                     avg_communication=Avg(
                                                                         'rate_communication'),
                                                                     avg_organize=Avg(
                                                                         'rate_organize'),
                                                                     avg_problem_solving=Avg(
                                                                         'rate_problem_solving'),
                                                                     avg_personality=Avg(
                                                                         'rate_personality'),
                                                                     avg_reliability=Avg(
                                                                         'rate_reliability'),
                                                                     avg_honesty_integrity=Avg(
                                                                         'rate_honesty_integrity'),
                                                                     avg_emotional_intelligence=Avg(
                                                                         'rate_emotional_intelligence'),
                                                                     avg_willingness_to_learn=Avg('rate_willingness_to_learn'))
    # PAGINATOR
    paginator = Paginator(user_review, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': user,
        'user_review': user_review,
        'avg_rating': avg_rating,
        'page_obj': page_obj,
    }
    return render(request, 'users/user_details.html', context)


@login_required
def users_list(request):
    offices = UserWorkOffice.objects.all()

    # PAGINATOR
    paginator = Paginator(offices, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'offices': offices,
        'page_obj': page_obj,
    }
    return render(request, 'users/users_list.html', context)


@login_required
def list_of_offices(request):
    offices = UserWorkOffice.objects.order_by("office_name")
    context = {
        'offices': offices,
    }
    return render(request, 'users/list_of_offices.html', context)


@login_required
def list_of_users_by_office(request, office_slug):
    offices = UserWorkOffice.objects.all()
    queryset = User.objects.all()
    if office_slug:
        work_office = get_object_or_404(UserWorkOffice, slug=office_slug)
        queryset = queryset.filter(work_office=work_office)

    context = {
        'offices': offices,
        'queryset': queryset,
        'work_office': work_office
    }
    return render(request, 'users/list_of_users_by_office.html', context)


def register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.phone_number = registerForm.cleaned_data['phone_number']
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
            user.work_office = registerForm.cleaned_data['work_office']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            # registerForm.save_m2m()
            login(request, user)
            return redirect("/home")
    else:
        registerForm = RegistrationForm()
    return render(request, 'users/register.html', {'form': registerForm})


@login_required
def edit_user(request, pk):

    if request.method == 'POST':
        editForm = EditUserForm(request.POST, instance=request.user)
        if editForm.is_valid():
            editForm.save()
            return redirect('users:user_details', pk=pk)
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        editForm = EditUserForm(instance=request.user)

    return render(request, 'users/edit_user.html', {'form': editForm})
