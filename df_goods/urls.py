#__author: "haichong"
#date: 2018/10/25
from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^list(\d+)_(\d+)_(\d+)/$', views.list, name="list"),
    re_path(r'^(\d+)/$', views.detail, name="detail"),
]