from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import OrderProductForm
from django.template.context_processors import csrf

# Create your views here.
def orders(request):
    if request.method == 'POST':
        order_product_form = OrderProductForm(request.POST)

        if order_product_form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        order_product_form = OrderProductForm()

    return render(request, 'order-product.html', {'order_product_form': order_product_form})
