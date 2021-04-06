from django.shortcuts import render

from .models import Order, OrderMaterials
from Material.models import Material
from MaterialPrice.views import get_current_price

def all_orders(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    orders = Order.objects.all()
    context['orders'] = orders

    return render(request, 'order/all_orders.html', context)

def view_order(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    order = Order.objects.get(id=id)

    order_materials_object = get_order_materials(id)

    context['order'] = {
        'order_object': order,
        'materials': get_order_materials(order.id)
    }

    print(context)
    return render(request, 'order/view_order.html', context)

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
