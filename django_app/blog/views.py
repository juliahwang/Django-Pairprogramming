from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)