from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'appblog/index.html', {'title': 'Index'})


def show_posts(request):
    posts = models.Post.objects.all()

    context = {'title': 'Show Posts',
               'posts': posts,
               }
    return render(request, 'appblog/show_posts.html', context=context)


def detail_post(request, post_id):
    post = models.Post.objects.get(pk=post_id)

    context = {'title': 'Detail Post',
               'post': post,
               }
    return render(request, 'appblog/detail_post.html', context=context)
