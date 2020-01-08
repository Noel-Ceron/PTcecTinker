# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from webservice import views

urlpatterns =[
        url(r'^tv_interruptor/$', views.interruptor),
        url(r'^vol_interruptor/$', views.vol),
        url(r'^mute_interruptor/$', views.mudo),
        url(r'^tinker_interruptor/$', views.interruptor_T),
        ]
