from django.urls import path
from django.conf.urls import include
from .views import all_clients, view_client

urlpatterns = [
    path('', all_clients, name='all_clients'),
    path('view/<id>', view_client, name='view_client'),
]
