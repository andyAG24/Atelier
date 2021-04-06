from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from .models import Order, OrderMaterials
from Material.models import Material
from MaterialPrice.views import get_current_price
from Fitting.views import get_fittings

def all_orders(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    context['orders'] = get_orders()

    return render(request, 'order/all_orders.html', context)

def view_order(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    order = Order.objects.get(id=id)

    order_materials_object = get_order_materials(id)

    context['order'] = {
        'order_object': order,
        'localized_status': get_localized_status(order.status),
        'localized_payment_status': get_localized_payment_status(order.payment_status),
        'localized_urgency': get_localized_urgency(order.urgency),
        'localized_labour_intensity': get_localized_labour_intensity(order.labour_intensity),
        'materials': get_order_materials(order.id),
        'fittings': get_fittings(order)
    }

    return render(request, 'order/view_order.html', context)

def get_orders():
    orders = Order.objects.all()
    orders_list = []
    for order in orders:
        orders_list.append({
            'order_object': order,
            'localized_status': get_localized_status(order.status),
            'localized_payment_status': get_localized_payment_status(order.payment_status),
            'localized_urgency': get_localized_urgency(order.urgency),
            'localized_labour_intensity': get_localized_labour_intensity(order.labour_intensity),
        })
    return orders_list

def get_client_orders(id):
    orders = Order.objects.filter(id_client=id)
    orders_list = []
    for order in orders:
        orders_list.append({
            'order_object': order,
            'localized_status': get_localized_status(order.status),
            'localized_payment_status': get_localized_payment_status(order.payment_status),
            'localized_urgency': get_localized_urgency(order.urgency),
            'localized_labour_intensity': get_localized_labour_intensity(order.labour_intensity),
        })
    return orders_list

def get_order_materials(id_order):
    order_materials_object = OrderMaterials.objects.filter(id_order=id_order)

    materials_list = []
    for item in order_materials_object:
        quantity = item.material_quantity
        price = get_current_price(item.id_material.id)
        cost = quantity * price
        kek = {
            'material_object': Material.objects.get(id=item.id_material.id),
            'quantity': quantity,
            'price': price,
            'cost': cost 
        }
        materials_list.append(kek)
    
    return materials_list

def get_localized_status(status):
    order_statuses = {
        'Created': _('Created'),
        'Cancelled': _('Cancelled'),
        'In progress': _('In progress'),
        'Completed': _('Completed'),
        'Passed to the client': _('Passed to the client'),
        'Returned for rework': _('Returned for rework')
    }
    return order_statuses[status]
    
def get_localized_payment_status(payment_status):
    payment_statuses = {
        'Pending payment': _('Pending payment'),
        'Prepayment made': _('Prepayment made'),
        'Paid': _('Paid')
    }
    return payment_statuses[payment_status]

def get_localized_urgency(urgency):
    urgencies = {
        'Low': _('Low urgency'),
        'Medium': _('Medium urgency'),
        'High': _('High urgency'),
        'Very high': _('Very high urgency')
    }
    return urgencies[urgency]

def get_localized_labour_intensity(labour_intensity):
    labour_intensities = {
        'Low': _('1-3 days'),
        'Medium': _('4-6 days'),
        'High': _('7-9 days'),
        'Very high': _('10+ days')
    }
    return labour_intensities[labour_intensity]

