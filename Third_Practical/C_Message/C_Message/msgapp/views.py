# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 01:22:36 2023

@author: Doha Thabet
"""

from django.shortcuts import render
from datetime import datetime 
from django.http import HttpResponse, JsonResponse, FileResponse
import os
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotAllowed, JsonResponse, StreamingHttpResponse, FileResponse
from django.core.files import File

def cloud(request):
    datalist = []
    # Check if the request method is POST
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        # Append the message data to the file
        with open("data.txt", 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    
    userC = request.GET.get("userC", None)
    # Check if userC is not None
    if userC is not None:
        with open("data.txt", 'r') as f:
            counter = 0
            # Iterate through each line in the file
            for line in f:
                linedata = line.strip().split('--')
                # Check if the first item in the line matches userC
                if linedata[0] == userC:
                    counter += 1
                    # Create a dictionary with message data and add it to the datalist
                    d = {"userA": linedata[1], 'msg': linedata[2], 'time': linedata[3]}
                    datalist.append(d)
                # Break the loop if the counter reaches 10
                if counter >= 10:
                    break
    print(datalist)  # Add this line to check the value of datalist
    return render(request, "MsgSingleWEb.html", {"data": datalist})






def my_responsetype(request):
    # Returns a simple HTTP response with the content 'Hello, world!'
    response = HttpResponse('Hello, this is HTTP Response')
    return response


def my_responsetype2(request):
    # Performs a permanent redirect to 'https://www.rtu.lv/en'
    response = HttpResponseRedirect('https://www.rtu.lv/en')
    return response


def my_responsetype3(request):
    # Returns an HTTP response indicating a bad request
    response = HttpResponseBadRequest('This is a BAD request')
    return response


def my_responsetype4(request):
    # Returns an HTTP response indicating that the requested page was not found
    response = HttpResponseNotFound('Page not found :(')
    return response
       


def my_responsetype5(request):
    # Returns an HTTP response indicating an internal server error
    response = HttpResponseServerError('Internal server error')
    return response


def my_responsetype6(request):
    # Returns an HTTP response indicating that the requested HTTP method is not allowed
    response = HttpResponseNotAllowed(['GET', 'POST'])
    return response


def my_responsetype7(request):
    # Returns a JSON response with data {'foo': 'bar'}
    data = {'foo': 'bar'}
    response = JsonResponse(data)
    return response


def my_streaming_view(request):
    # Generates a streaming HTTP response with a sequence of numbers from 0 to 9
    def stream_response():
        for i in range(10):
            yield str(i)

    response = StreamingHttpResponse(stream_response())
    return response


def my_responsetype8(request):
    # Returns a file response for a PDF file named 'd.pdf'
    file = File(open('d.pdf', 'rb'))
    response = FileResponse(file)
    return response


def video_view(request):
    video_file_path = 'dd.mp4'  # Replace with the actual path to your video file

    # Returns a file response for a video file with content type 'video/mp4'
    response = FileResponse(open(video_file_path, 'rb'), content_type='video/mp4')
    return response


def my_responsetype9(request):
    # Performs a permanent redirect to 'https://www.rtu.lv/en'
    response = HttpResponsePermanentRedirect('https://www.rtu.lv/en')
    return response

