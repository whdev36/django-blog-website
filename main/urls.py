# urls.py

from django.urls import path
from . import views
from django.conf.urls import handler404, handler500, handler403, handler400

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
	path('turkum/<slug:slug>/', views.category, name='category'),
	path('teg/<slug:slug>/', views.tag, name='tag'),
]

handler404 = 'main.views.custom_404'
handler500 = 'main.views.custom_500'
handler403 = 'main.views.custom_403'
handler400 = 'main.views.custom_400'