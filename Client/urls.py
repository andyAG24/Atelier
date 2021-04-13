from django.urls import path
from django.conf.urls import include
from .views import all_clients, view_client, add_client, delete_client, EditClientView

urlpatterns = [
    path('', all_clients, name='all_clients'),
    path('view/<id>', view_client, name='view_client'),
    path('add', add_client, name='add_client'),
    path('delete/<id>', delete_client, name='delete_client'),
    path('edit/<int:pk>', EditClientView.as_view(), name='edit_client'),
]
