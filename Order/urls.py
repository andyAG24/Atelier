
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from .views import kek

urlpatterns = [
    # path('auth/', redirect_to_auth, name='auth'),
    path('view/', kek, name='view_orders')
]
