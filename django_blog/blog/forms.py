from django import forms
from . import models
from .models import Comment

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    fields = ['title','content']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']