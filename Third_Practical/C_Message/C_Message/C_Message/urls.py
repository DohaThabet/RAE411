"""
URL configuration for C_Message project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from msgapp import views as msgviews 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cloud_message/',include("msgapp.urls")),
    path('http_response/', msgviews.my_responsetype),
    path('Redirect/', msgviews.my_responsetype2),
    path('bad-request/', msgviews.my_responsetype3),
    path('not-found/', msgviews.my_responsetype4),
    path('server-error/', msgviews.my_responsetype5),
    path('not-allowed/', msgviews.my_responsetype6),
    path('json-r/', msgviews.my_responsetype7),
    path('stream/', msgviews.my_streaming_view),
    path('file/', msgviews.my_responsetype8),
    path('video/', msgviews.video_view),
    path('permanent-redirect/', msgviews.my_responsetype9),
]
