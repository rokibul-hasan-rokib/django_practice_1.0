from django import forms
from .models import Service
from blog.models import Blog 

class ServiceForm(forms.ModelForm):
    blog = forms.ModelChoiceField(queryset=Blog.objects.all(), label="Select Blog", empty_label="Select Blog", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Service
        fields = ['blog', 'title', 'icon', 'description']
