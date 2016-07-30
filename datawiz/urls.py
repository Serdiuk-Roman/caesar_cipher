from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^choice/$', views.LoginFormView.as_view(), name='choice'),
    url(r'^$', views.index, name='index'),
]
