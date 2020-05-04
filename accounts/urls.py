from django.conf.urls import url, include
from accounts.views import logout, registration, index, home
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^register/', registration, name="registration"),
    url(r'^home/', home, name='home'),
    url(r'^password-reset/', include(url_reset))
]
