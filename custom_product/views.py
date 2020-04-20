from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CustomProductForm
from django.template.context_processors import csrf

# Create your views here.
def custom_product_view(request):
    if request.method == 'POST':
        custom_product_form = CustomProductForm(request.POST)

        if custom_product_form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        custom_product_form = CustomProductForm()

    return render(request, 'custom_product.html', {'custom_product_form': custom_product_form})
