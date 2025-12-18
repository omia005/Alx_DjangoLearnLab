from django import forms
from . import models
from .models import Comment
from taggit.forms import TagWidget

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    fields = ['title','content', 'tag']
    widgets = {
            "tags": TagWidget(),
        }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']