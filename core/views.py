from django.db.models.aggregates import Sum
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum, F
from users.models import User, UserWorkOffice
from ratings.models import Review


@login_required
def home(request):
    users = User.objects.all()
    users_count = User.objects.count()
    offices = UserWorkOffice.objects.order_by("office_name")
    ratings = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        avg_professionalism=Avg('rate_professionalism'),
        avg_teamwork=Avg('rate_teamwork'),
        avg_communication=Avg('rate_communication'),
        avg_organize=Avg('rate_organize'),
        avg_problem_solving=Avg('rate_problem_solving'),
        avg_personality=Avg('rate_personality'),
        avg_reliability=Avg('rate_reliability'),
    ).order_by('-avg_professionalism')
    overall_ratings = Review.objects.values('reviewed_user__first_name', 'reviewed_user__last_name').annotate(
        all=Avg(F('rate_professionalism')+F('rate_teamwork')+F('rate_communication')+F('rate_organize')+F('rate_problem_solving')+F('rate_personality')+F('rate_reliability'))).order_by('-all')

    context = {
        'users': users,
        'offices': offices,
        'users_count': users_count,
        'ratings': ratings,
        'overall_ratings': overall_ratings,

    }
    return render(request, 'dashboard.html', context)
