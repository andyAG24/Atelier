# from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .models import MaterialPrice

def get_current_price(material_id):
    material_price = MaterialPrice.objects.filter(id_material=material_id)
    current_material_price = _('Undefined')
    if material_price:
        material_price = MaterialPrice.objects.filter(id_material=material_id).order_by('-modification_date')[0]
        current_material_price = material_price.price
    return current_material_price

def get_price_history(material_id):
    return MaterialPrice.objects.filter(id_material=material_id).order_by('-modification_date')
