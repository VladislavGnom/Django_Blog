from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import CommentForm


def index(request):
    return render(request, 'appblog/index.html', {'title': 'Index'})


def show_posts(request):
    posts = models.Post.objects.all()

    context = {'title': 'Show Posts',
               'posts': posts,
               }
    return render(request, 'appblog/show_posts.html', context=context)


def detail_post(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            
            return redirect('detail', post_id=post.pk)
    else:
        form = CommentForm()

    context = {'title': 'Detail Post',
               'post': post,
               'form': form,
               }
    return render(request, 'appblog/detail_post.html', context=context)
