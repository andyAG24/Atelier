"""Atelier URL Configuration

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
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from .views import mainpage_view, redirect_to_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage_view, name='main'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', redirect_to_auth, name='auth'),
    path('orders/', include('Order.urls')),
    path('materials/', include('Material.urls')),
    path('employees/', include('Employee.urls'))
]
