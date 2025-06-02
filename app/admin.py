from django.contrib import admin
from .models import Post, Comment, Tag, Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "updated_at"]
    list_filter = ["created_at", "author", "tags"]
    search_fields = ["title", "content"]
    date_hierarchy = "created_at"
    filter_horizontal = ["tags"]
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author","text", "created_at"]
    list_filter = ["created_at", "author"]
    search_fields = ["text"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "location"]
    search_fields = ["user__username", "location"]
