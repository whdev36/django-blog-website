from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

# --- POST MODEL ---
class Post(models.Model):
	title = models.CharField(max_length=255)  # title
	content = models.TextField()  # content
	author = models.ForeignKey(User, on_delete=models.CASCADE)  # author
	created_at = models.DateTimeField(auto_now_add=True)  # created date
	updated_at = models.DateTimeField(auto_now=True)  # updated date
	is_published = models.BooleanField(default=True)  # is publish
	claps = models.PositiveIntegerField(default=0)  # claps
	views = models.PositiveIntegerField(default=0)  # view 

	class Meta:
		# verbose_name = 'Post'
		# verbose_name_plural = 'Posts'
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	def add_clap(self, commit=True):
		self.claps += 1
		self.save()

	def add_view(self, commit=True):
		self.views += 1
		self.save()

	@classmethod
	def get_trending_posts(cls):
		return cls.objects.annotate(
			total_interactions=F('views') + F('claps')
			).order_by('-total_interactions', '-created_at')
