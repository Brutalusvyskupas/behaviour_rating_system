from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator

from .models import Post
from .forms import PostEditForm, CreatePostForm


def all_posts(request):
    posts = Post.objects.order_by("-date_posted")

    # PAGINATOR.
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

def create_post(request):
    form = CreatePostForm(request.POST or None)
    author = request.user
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect("/home")

    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'posts/create_post.html', context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts:post_details', pk=post.pk)
    else:
        form = PostEditForm(instance=post)
    
    context = {
        "form": form,
        "post": post
    }

    return render(request, 'posts/post_edit.html', context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:all_posts')
    context = {
        'post': post,
    }
    return render(request, 'posts/post_delete.html', context)
    

