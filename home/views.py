from django.shortcuts import render
from products.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})
