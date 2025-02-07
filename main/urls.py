# urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	# path('login/', views.login_user, name='login'),
	# path('register/', views.register_user, name='register'),
	# path('logout/'. views.logout_user, name='logout'),
	path('maqolalar/', views.posts, name='posts'),
	path('maqola/<int:pk>/', views.post, name='post'),
	path('maqola/<int:pk>/qarsak/', views.clap, name='clap'),
	path('qidiruv/', views.search, name='search'),
	path('turkumlar/', views.categories, name='categories'),
]