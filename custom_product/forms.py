from django import forms
from django.forms import ModelForm
from .models import CustomProduct

class CustomProductForm(forms.ModelForm):
    class Meta:
        model = CustomProduct
        fields = ('type', 'size', 'description')
