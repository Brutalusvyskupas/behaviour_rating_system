from os import name
from re import template
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import home
from users.forms import LoginForm

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html',
         form_class=LoginForm), name='login'),
    path('home/', home, name="home"),
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace="users")),
    path('', include('posts.urls', namespace="posts")),

    # Password reset links
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/registration/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/registration/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/registration/password_reset_form.html'), name='password_reset_form'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/registration/password_reset_complete.html'),
        name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)