from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post, Category
from django.http import JsonResponse
from django.db.models import F, Q

# --- HOME PAGE ---
def home(request):
	# posts = Post.objects.filter(is_published=True)
	posts = Post.get_trending_posts()
	return render(request, 'home.html', {'posts': posts})

# --- POSTS ---
def posts(request):
	posts = Post.objects.filter(is_published=True)
	return render(request, 'posts.html', {'posts': posts})

# --- POST ---
def post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.add_view()  # update post view
	return render(request, 'post.html', {'post': post})

# --- CLAP ---
def clap(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.add_clap()
	# return redirect('post', pk=post.pk)
	# post.claps = F('claps') + 1
	# post.save(update_fields=['claps'])
	# post.refresh_from_db()
	return JsonResponse({'success': True, 'claps': post.claps})


# --- SEARCH ---
def search(request):
	query = request.GET.get('q', '')
	results = []
	if query:
		results = Post.objects.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(tags__name__icontains=query)
		).distinct()
	return render(request, 'search.html', {'query': query, 'results': results})

def categories(request):
	categories = Category.objects.all()
	return render(request, 'categories.html', {'categories': categories})