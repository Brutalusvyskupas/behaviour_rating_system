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

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
