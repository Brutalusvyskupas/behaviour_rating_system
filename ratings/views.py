from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.db.models import Avg, Sum

from users.models import User
from .models import Review
from .forms import RateForm


@login_required
def rate_user(request, pk):
    r_user = get_object_or_404(User, pk=pk)

    # if request.user == r_user:
    #     messages.error(request, 'You cannot rate yourself!')
    #     return redirect('users:list_of_users')

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewed_by = request.user
            review.reviewed_by.save()
            review.reviewed_user = r_user
            review.save()
            return redirect('users:user_details', pk=r_user.pk)
    else:
        form = RateForm()

    return render(request, 'ratings/rate.html', {'form': form, 'r_user': r_user})


@login_required
def all_ratings(request):
    ratings = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        avg_professionalism=Avg('rate_professionalism'),
        avg_teamwork=Avg('rate_teamwork'),
        avg_communication=Avg('rate_communication'),
        avg_organize=Avg('rate_organize'),
        avg_problem_solving=Avg('rate_problem_solving'),
        avg_personality=Avg('rate_personality'),
        avg_reliability=Avg('rate_reliability'),
    ).order_by('reviewed_user')
    context = {
        'ratings': ratings,
    }
    return render(request, 'ratings/all_ratings.html', context)
