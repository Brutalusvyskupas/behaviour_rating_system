from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def all_posts(request):
    posts = Post.objects.order_by("-date_posted")

    # PAGINATOR
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, "posts/all_posts.html", context)

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post':post,
    }
    return render(request, "posts/post_details.html", context)