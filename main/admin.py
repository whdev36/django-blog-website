from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Category, Tag


# Register
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'created_at', 'updated_at', 'is_published']
	list_filter = ['is_published', 'created_at']
	search_fields = ['title', 'content']
	filter_horizontal = ('tags',)

class TagAdmin(admin.ModelAdmin):
	list_display = ['name']
	search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	search_fields = ['name', 'slug']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.unregister(Group)