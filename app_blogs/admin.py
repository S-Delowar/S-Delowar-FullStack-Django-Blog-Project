from django.contrib import admin

from app_blogs.models import Blog, Comment, Like

# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine,]
    list_display = ("title", "author", "publish_date", "total_comments", "total_likes")

    def total_comments(self, obj):
        return obj.total_comments()
    
    def total_likes(self, obj):
        return obj.total_likes()
    
    total_comments.short_description = 'Total Comments'
    total_likes.short_description = 'Total Likes'
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Like)