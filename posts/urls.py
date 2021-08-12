from django.urls import path


from .views import post_details, all_posts


app_name = 'posts'

urlpatterns = [
    path('posts/', all_posts, name="all_posts"),
    path('posts/<int:pk>/', post_details, name='post_details'),
]
