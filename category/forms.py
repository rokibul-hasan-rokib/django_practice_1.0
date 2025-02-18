from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100, error_messages={'required': 'Name is required.'})

    class Meta:
        model = Category
        fields = ['name','status'] 
