from django.conf.urls import url
from .views import index_pro


urlpatterns = [
    url(r'^proyecto$', index_pro, name='index_pro'),
]