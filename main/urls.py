# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	# path('login/', views.login_user, name='login'),
	# path('register/', views.register_user, name='register'),
	# path('logout/'. views.logout_user, name='logout'),
	path('posts/', views.posts, name='posts'),
	path('post/<int:pk>/', views.post, name='post'),
]