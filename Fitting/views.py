from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .models import Fitting

def get_fittings(order):
    fittings = Fitting.objects.filter(id_order=order)
    list = []
    for fitting in fittings:
        list.append({
            'fitting_object': fitting,
            'localized_fitting_status': get_localized_fitting_status(fitting.status)
        })
    return list

def get_localized_fitting_status(status):
    fitting_statuses = {
        'Created': _('Created'),
        'The client is called for fitting': _('The client is called for fitting'),
        'The product fits in size': _('The product fits in size'),
        'There are flaws': _('There are flaws') 
    }
    return fitting_statuses[status]
