from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from users.models import User
from .forms import RateForm


@login_required
def rate_user(request, pk):
    r_user = get_object_or_404(User, pk=pk)

    if request.user == r_user:
        messages.error(request, 'You cannot rate yourself!')
        return redirect('users:list_of_users')
        
    else:   
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
