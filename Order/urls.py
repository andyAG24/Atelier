
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from .views import all_orders, view_order

urlpatterns = [
    path('', all_orders, name='all_orders'),
    path('view/<id>', view_order, name='view_order'),
]
