from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_fronted = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_fronted)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post':post}
    return render(request, 'blog/post_detail.html', stuff_for_frontend)