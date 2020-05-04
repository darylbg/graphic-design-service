from django.conf.urls import url
from .views import orders



urlpatterns = [
    url(r'^$', orders, name='orders'),
]
