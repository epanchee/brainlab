"""brain_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from brain_lab import views
from brain_lab.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time_to_servey/$', views.time_to_servey, name='time_to_servey'),
    url(r'visitor-autocomplete/$', VisitorAutocomplete.as_view(), name='visitor-autocomplete'),
    url(r'^$', RedirectView.as_view(url='admin/', permanent=False), name='index'),
]
