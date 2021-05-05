from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, dashboard, users_list
from .forms import LoginForm


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/users/login/'), name="logout"),
    path('users/', users_list, name='users'),
    path('dashboard/<uuid:pk>/', dashboard, name='dashboard'),
    path('register/', register, name="register"),
]