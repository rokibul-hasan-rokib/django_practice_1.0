from django import forms
from .models import Blog, Category

class BlogForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        max_length=100,
        error_messages={'required': 'Title is required.'}
    )
    name = forms.CharField(
        required=True,
        max_length=100,
        error_messages={'required': 'Name is required.'}
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        empty_label="Select a Category",
        error_messages={'required': 'Category is required.'}
    )

    class Meta:
        model = Blog
        fields = ['category', 'name', 'title', 'description', 'image']
