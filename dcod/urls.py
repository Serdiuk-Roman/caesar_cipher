from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.coder, name='coder'),
    url(r'^cipher/$', views.caesar_cipher, name='cipher'),
]
