from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from . import models
from .forms import CommentForm, EditPostForm, CreatePostForm
from django.contrib.auth.decorators import login_required


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


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)

    if post.author == request.user:
        if request.method == "POST":
            edit_form = EditPostForm(data=request.POST, instance=post)

            if edit_form.is_valid():
                post.title = edit_form.data.get('title')
                post.content = edit_form.data.get('content')
                
                post.save()

                return redirect('edit_post', post_id=post.pk)
        else:
            edit_form = EditPostForm(instance=post)

        context = {'title': 'Edit Post',
                'form': edit_form,
                'post': post,
                }

        return render(request, 'appblog/edit_post.html', context=context)
    else:
        return HttpResponseForbidden("<h1>403 Forbidden</h1>")


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(models.Post, pk=post_id)
    # post_pk = post.pk

    if request.method == 'POST':
        post.delete()

    return redirect('user_posts', username=request.user)


@login_required
def create_post(request):
    if request.method == "POST":
        create_form = CreatePostForm(request.POST)

        if create_form.is_valid():
            new_post = create_form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect('user_posts', username=request.user)
    else:
        create_form = CreatePostForm()

    context = {'title': 'Create Post',
               'form': create_form,
               }
    return render(request, 'appblog/create_post.html', context=context)



def user_post_display(request, username):
    posts = models.Post.objects.filter(author=request.user)

    context = {'title': 'All Posts',
               'posts': posts,
               }

    return render(request, 'appblog/user_post_display.html', context=context)
