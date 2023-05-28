# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 02:07:28 2023

@author: Doha Thabet
"""
from django.http import HttpResponse
def Hello(request):
    return HttpResponse("Hello world! I am coming...")
