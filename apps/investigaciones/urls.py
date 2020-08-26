from django.conf.urls import url
from .views import index_inv

app_name = 'investigaciones'
urlpatterns = [
    url(r'^investigaciones$', index_inv, name='index_inv'),
]