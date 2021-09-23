from django import forms
from django.db.models import fields
from .models import Blog, Comment, Youtube

class BlogForm(forms.ModelForm):
    class Meta:
      model = Blog
      fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = ['subtitle','body','url']