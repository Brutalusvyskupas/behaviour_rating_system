from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, F, Count, Q
from users.models import User, UserWorkOffice
from ratings.models import Review


@login_required
def home(request):
    users = User.objects.all()
    offices = UserWorkOffice.objects.order_by("office_name")
    context = {
        'users': users,
        'offices': offices,

    }
    return render(request, 'dashboard.html', context)
