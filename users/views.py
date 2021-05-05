from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login

from .forms import RegistrationForm
from .models import User, UserWorkOffice


def dashboard(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'users/dashboard.html', context)


def users_list(request):
    offices = UserWorkOffice.objects.all()
    context = {
        'offices': offices,
    }
    return render(request, 'users/users_list.html', context)


# def list_of_users_by_office(request, office_slug):
#     offices = UserWorkOffice.objects.all()
#     users = User.objects.all()
#     if office_slug:
#         office = get_object_or_404(UserWorkOffice, slug=office_slug)
#         user = users.filter(work_office=work_office)
#     context = {
#         'offices': offices,
#         'office': office,
#         'users': users,
#         'user': user
#     }
#     return render(request, 'users/list_of_users_by_office.html', context)


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
            registerForm.save_m2m()
            login(request, user)
            return redirect("/")
    else:
        registerForm = RegistrationForm()
    return render(request, 'users/register.html', {'form': registerForm})
