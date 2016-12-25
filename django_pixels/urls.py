# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'pixel/$', views.pixel, name='pixel'),
    url(r'pixel204/$', views.pixel204, name='pixel-204'),
]
