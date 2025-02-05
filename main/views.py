from django.shortcuts import render
from django.contrib import messages
from .models import Post

# --- HOME PAGE ---
def home(request):
	posts = Post.objects.filter(is_published=True)
	return render(request, 'home.html', {'posts': posts})

# --- POSTS ---
def posts(request):
	posts = Post.objects.filter(is_published=True)
	return render(request, 'posts.html', {'posts': posts})

# --- POST ---
def post(request, pk):
	return render(request, 'post.html', {})
