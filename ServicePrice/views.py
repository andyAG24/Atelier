# from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .models import ServicePrice
from Service.models import Service

def get_current_price(service_id):
    service_price = ServicePrice.objects.filter(id_service=service_id)
    current_service_price = _('Undefined')
    if service_price:
        service_price = ServicePrice.objects.filter(id_service=service_id).order_by('-modification_date')[0]
        current_service_price = service_price.price
    return current_service_price

def get_price_history(service_id):
    return ServicePrice.objects.filter(id_service=service_id).order_by('-modification_date')
