from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        print(f"Post: {post}")
        return render(request, 'blog/post_detail.html', {'post': post})
    except Http404:
        print("Post not found!")
        return render(request, 'blog/404.html', status=404)
    except Exception as e:
        # Log the exception
        print(f"Error in post_detail view: {e}")
        logger.exception(f"Error in post_detail view: {e}")
        # Render a generic error page
        return render(request, 'blog/error.html', {'error_message': str(e)}, status=500)

