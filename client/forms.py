from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    "name" = forms.CharField(required=True, max_length=100, error_messages={'required': 'Name is required.'})
    class Meta:
        model = Client
        fields = ['name', 'designation']
