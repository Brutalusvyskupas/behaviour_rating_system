
from ratings.models import Review
from django.shortcuts import redirect, render, get_object_or_404
from django.urls.base import reverse
from django.contrib.auth.decorators import login_required

from users.models import User
from .forms import RateForm


@login_required
def rate_user(request, pk):
    r_user = get_object_or_404(User, pk=pk)

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

    return render(request, 'ratings/rate.html', {'r_user': r_user, 'form': form})
