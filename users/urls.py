from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register
from .forms import LoginForm


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login/'), name="logout"),
    path('register/', register, name="register"),
]