# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 03:25:04 2023

@author: Doha Thabet
"""
from django.shortcuts import render
def Hello2(request):
    return render (request,'Hello.html')
