from django.db import models
from django.contrib.auth.models import User

# --- POST MODEL ---
class Post(models.Model):
	title = models.CharField(max_length=255)  # title
	content = models.TextField()  # content
	author = models.ForeignKey(User, on_delete=models.CASCADE)  # author
	created_at = models.DateTimeField(auto_now_add=True)  # created date
	updated_at = models.DateTimeField(auto_now=True)  # updated date
	is_published = models.BooleanField(default=True)  # is publish

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
		ordering = ['-created_at']
