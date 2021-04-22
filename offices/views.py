from django.shortcuts import render

from .models import WorkOffice

def list_of_offices(request):
    offices = WorkOffice.objects.all()
    context = {
        'offices': offices,
    }
    return render(request, 'offices/list_of_offices.html', context)
