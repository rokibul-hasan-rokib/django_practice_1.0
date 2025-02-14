from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=100, error_messages={'required': 'Title is required.'})
    name = forms.CharField(required=True, max_length=100, error_messages={'required': 'Name is required.'})

    class Meta:
        model = Blog
        fields = ['name', 'title', 'description', 'image']
