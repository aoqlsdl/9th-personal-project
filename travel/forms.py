from django import forms
from django.db.models import fields
from django.db.models.base import Model
from .models import Comment, ImageUpload, Record
from travel import models

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name', 'comment_text')

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ['title', 'image', 'post']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['title', 'body', 'pub_date', 'hashtag', 'image']