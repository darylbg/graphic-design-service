from django.conf.urls import url
from .views import custom_product_view

urlpatterns = [
    url(r'^$', custom_product_view, name='custom-product-view')
]
