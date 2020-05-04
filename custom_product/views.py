from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .forms import OrderProductForm
from django.template.context_processors import csrf
from cart.views import view_cart, add_to_cart

# Create your views here.
def orders(request):
    if request.method == 'POST':
        order_product_form = OrderProductForm(request.POST)

        if order_product_form.is_valid():
            order_product_form.save()

            return redirect(reverse('view_cart'))

    else:
        order_product_form = OrderProductForm()


    return render(request, 'order-product.html', {'order_product_form': order_product_form})
