# from ratings.models import Review
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.db.models import Avg


from users.models import User
from .forms import RateForm


@login_required
def rate_user(request, pk):
    r_user = get_object_or_404(User, pk=pk)
    # score = Review.objects.all().aggregate(Avg('rate_professionalism'), Avg('rate_teamwork'), Avg('rate_communication'),
    #                                        Avg('rate_organize'), Avg('rate_problem_solving'), Avg('rate_personality'), Avg('rate_reliability')) #

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

    return render(request, 'ratings/rate.html', {'form': form})
