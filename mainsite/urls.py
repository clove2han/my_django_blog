#_*_coding:utf-8_*_

"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainsite.views import homepage,showpost,current_datetime,moments_input
urlpatterns = [

    url(r'^$', homepage),
#把post/开头的网址后面的字符串都找出来。
    url(r'^post/(\w+)$', showpost),
    url(r'^current_datetime',current_datetime,name='current_datetime'),
    url(r'^input', moments_input,name='input'),

]
