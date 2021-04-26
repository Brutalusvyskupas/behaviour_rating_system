from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


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
