"""pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

from app3 import views

app_name = "app3"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^book/', views.book, name='book'),
    url(r'^books/(?P<pk>\d+)/$', views.delete_book, name='delete_book'),
    url(r'^view_book/(?P<pk>\d+)/$', views.view_book, name='view_book'),
    url(r'^edit_book/(?P<pk>\d+)/$', views.edit_book, name='edit_book'),
    url(r'^search/', views.search, name='search'),
    # url(r'^setsession/', views.setsession, name='setsession'),
    # url(r'^getsession/', views.getsession, name='getsession'),
]
