from django import forms
from .models import Book
from .models import ExampleForm

class ExampleForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
