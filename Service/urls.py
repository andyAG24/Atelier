from django.urls import path
from django.conf.urls import include
from .views import all_services, view_service

urlpatterns = [
    # path('auth/', redirect_to_auth, name='auth'),
    path('', all_services, name='all_services'),
    path('view/<id>', view_service, name='view_service')
]