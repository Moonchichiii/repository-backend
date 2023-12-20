from django.contrib import admin
from .models import Post

# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'updated_at', 'published')
    list_filter = ('published', 'created_at')
    search_fields = ('title', 'content', 'user__username')
    actions = ['publish_posts', 'unpublish_posts']


    def publish_posts(self, request, queryset):
        queryset.update(published=True)
    publish_posts.short_description = "Mark selected posts as published"

    
    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
    unpublish_posts.short_description = "Mark selected posts as unpublished"