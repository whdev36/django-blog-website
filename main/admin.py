from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post


# Register
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'created_at', 'updated_at', 'is_published']
	list_filter = ['is_published', 'created_at']
	search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)

admin.site.unregister(Group)