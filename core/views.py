from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.models import User, UserWorkOffice
from posts.models import Post

# home
@login_required
def home(request):
    users = User.objects.all()
    posts = Post.objects.order_by("-date_posted")[:4]
    offices = UserWorkOffice.objects.order_by("office_name")
    context = {
        'users': users,
        'posts': posts,
        'offices': offices,

    }
    return render(request, 'dashboard.html', context)

