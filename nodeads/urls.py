from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^$', views.weather, name='weather'),
    url(r'^owmo/$', views.owmo, name='owmo'),
    url(r'^ajax/$', views.ajax, name='ajax'),
    url(r'^$', views.owm, name='owm'),
]
