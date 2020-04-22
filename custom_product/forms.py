from django import forms
from django.forms import ModelForm
from products.models import Product

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('type', 'size', 'description')
