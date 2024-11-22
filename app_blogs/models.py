from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

# Blog Model
class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=240)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    cover_img = models.ImageField(upload_to="cover_images", blank=True, null=True)
    content = models.TextField(default='')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return f"{self.title[:30]}.............."

    def get_absolute_url(self):
        return reverse("blog_detail", args=[str(self.id)])

    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()
    
    
# Comment Model
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=350)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.user} on {self.blog.title[:100]}'


# Like Model
class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='likes')
    
    def __str__(self):
        return f"{self.user} likes {self.blog.title[:100]}"
    
