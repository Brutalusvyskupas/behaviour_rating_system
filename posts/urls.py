from django.urls import path


from .views import post_details, all_posts, post_edit, post_delete, create_post


app_name = 'posts'

urlpatterns = [
    path('posts/', all_posts, name="all_posts"),
    path('create_post/', create_post, name='create_post'),
    path('posts/<int:pk>/', post_details, name='post_details'),
    path('posts/<int:pk>/post_edit/', post_edit, name='post_edit'),
    path('posts/<int:pk>/post_delete/', post_delete, name='post_delete'),
]
