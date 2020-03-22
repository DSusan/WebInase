from django.conf.urls import url
from .views import index_inv


urlpatterns = [
    url(r'^investigaciones$', index_inv, name='index_inv'),
]