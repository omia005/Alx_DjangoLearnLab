from django import forms
from . import models
from .models import Comment

class CreatePostForm(forms.ModelForm):
  class Meta:
    model = models.Post
    fields = ['title','content', 'tag']

    TagWidgets = {
      'tag': forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'}),
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']