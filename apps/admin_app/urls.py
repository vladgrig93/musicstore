from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^admin_portal$', views.index),]
    