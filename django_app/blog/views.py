from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from blog.models import Post

User = get_user_model()
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    if request.method == "GET":
        context = {

        }
        return render(request, 'blog/post_add.html', context)
    elif request.method == 'POST':
        data = request.POST
        post = Post.objects.create(
            author=User.objects.first(),
            title=data['titlebox'],
            text=data['textbox'],
        )
        print('request: ', request.POST)
        return redirect('post_detail', pk=post.pk)


def post_modify(request, pk):
    post = Post.objects.get(pk = pk)
    if request.method == 'GET':
        context = {
            'title': post.title,
            'text': post.text,
        }
        return render(request, 'blog/post_modify.html', context)
    elif request.method == 'POST':
        data = request.POST
        post.title = data['titlebox']
        post.text = data['textbox']
        post.save()
        return redirect('post_detail', pk=post.pk)


def post_delete(request):
    if request.method == 'POST':
        print('post')
        # post = Post.objects.get(id=pk)
        post.delete()
        return render(request, 'blog/post_delete.html')

    elif request.method == 'GET':
        # post = get_object_or_404(Post, id = pk)
        # context = {
        #     'post': post,
        # }
        print('get')
        return render(request, 'blog/post_detail.html')







