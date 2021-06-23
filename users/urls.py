from django.urls import path
from django.contrib.auth import views as auth_views

from .views import register, users_list, list_of_offices, list_of_users_by_office, user_details, edit_user, search
from ratings.views import rate_user, all_ratings
from .forms import LoginForm


app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
         form_class=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name="logout"),
    path('search/', search, name="search"),
    path('offices/', list_of_offices, name='list_of_offices'),
    path('offices/<str:office_slug>/', list_of_users_by_office,
         name='list_of_users_by_office'),
    path('statistics/', all_ratings, name='all_ratings'),
    path('users/', users_list, name='list_of_users'),
    path('users/<uuid:pk>/', user_details, name='user_details'),
    path('users/<uuid:pk>/edit_user/', edit_user, name='edit_user'),
    path('users/<uuid:pk>/rate/', rate_user, name='rate_user'),
    path('register/', register, name="register"),
]
