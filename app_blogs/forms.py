from django import forms

from app_blogs.models import Blog, Comment

class BlogCreationForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "cover_img", "content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]