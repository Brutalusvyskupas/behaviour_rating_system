from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, users_list, list_of_offices, list_of_users_by_office, user_details
from .forms import LoginForm


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
         form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name="logout"),
    path('offices/', list_of_offices, name='list_of_offices'),
    path('offices/<str:office_slug>/', list_of_users_by_office,
         name='list_of_users_by_office'),
    path('users/', users_list, name='list_of_users'),
    path('users/<uuid:pk>/', user_details, name='user_details'),
    path('register/', register, name="register"),
]
