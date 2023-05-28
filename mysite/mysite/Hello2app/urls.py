# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 03:24:51 2023

@author: Doha Thabet
"""

from django.urls import path
from . import views
urlpatterns = [
   path('', views.Hello2),]