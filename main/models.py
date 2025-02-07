from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from django.utils.text import slugify
import markdown
# import markdown2
import bleach


# --- CATEGORY MODEL ---
class Category(models.Model):
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['name']

	name = models.CharField(max_length=150, unique=True)  # name
	slug = models.SlugField(max_length=150, blank=True, null=True, unique=True)  # category

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

class Tag(models.Model):
	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'
		ordering = ['name']

	name = models.CharField(max_length=150, unique=True)  # name
	slug = models.SlugField(max_length=150, blank=True, null=True, unique=True)  # slug of tag

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

# --- POST MODEL ---
class Post(models.Model):
	title = models.CharField(max_length=255)  # title
	content = models.TextField()  # content
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # author
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')  # category
	tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # tags
	sources = models.TextField(blank=True, null=True)  # sources
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
		# self.claps = F('claps') + 1
		# self.save(update_fields=['claps'])
		self.claps += 1
		self.save()

	def add_view(self, commit=True):
		# self.views = F('views') + 1
		# self.save(update_fields=['views'])
		self.views += 1
		self.save()

	@classmethod
	def get_trending_posts(cls, limit=10):
		return cls.objects.annotate(
			total_interactions=F('views') + F('claps')
		).order_by('-total_interactions', '-created_at')[:limit]

	def get_markdown_content(self):
		raw_html = markdown.markdown(self.content, extensions=['extra'])
		allowed_tags = ['p', 'a', 'b', 'i', 'strong', 'em', 'ul', 'ol', 'li', 'code',
			'img', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'br', 'pre', 'span', 'div']
		allowed_attributes = {
			'a': ['href', 'title'],
			'img': ['src', 'alt', 'width', 'height'],
			'span': ['class', 'id'],
			'div': ['class', 'id'],
		}
		return bleach.clean(raw_html, tags=allowed_tags, attributes=allowed_attributes, protocols=['https', 'http'])

	def get_markdown_sources(self):
		if not self.sources:
			return ""
		raw_html = markdown.markdown(self.sources, extensions=['extra'])
		allowed_tags = ['p', 'a', 'b', 'i', 'strong', 'em', 'ul', 'ol', 'li', 'code']
		allowed_attributes = {
			'a': ['href', 'title'],
		}
		return bleach.clean(raw_html, tags=allowed_tags, attributes=allowed_attributes, protocols=['https', 'http'])

	def get_author(self):
		if self.author.first_name and self.author.last_name:
			return f'{self.author.first_name} {self.author.last_name}'
		
		return self.author.username