#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from Control import views

urlpatterns = [
    url(r'^host_list/', views.host_list, name='host_list'),
]