from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from django.utils.text import slugify


# --- CATEGORY MODEL ---
class Category(models.Model):
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	name = models.CharField(max_length=150)
	slug = models.SlugField(max_length=150, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name.lower())
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

class Tag(models.Model):
	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

# --- POST MODEL ---
class Post(models.Model):
	title = models.CharField(max_length=255)  # title
	content = models.TextField()  # content
	author = models.ForeignKey(User, on_delete=models.CASCADE)  # author
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # category
	tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # tags
	created_at = models.DateTimeField(auto_now_add=True)  # created date
	updated_at = models.DateTimeField(auto_now=True)  # updated date
	is_published = models.BooleanField(default=True)  # is publish
	claps = models.PositiveIntegerField(default=0)  # claps
	views = models.PositiveIntegerField(default=0)  # view 

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
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
