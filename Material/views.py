from django.shortcuts import render
from MaterialPrice.views import get_current_price, get_price_history
from .models import Material

def all_materials(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    material_list = []
    materials = Material.objects.all()
    for material in materials:
        material_list.append(
            {
                'material': material,
                'material_price': get_current_price(material.id)
            }
        )
    context['materials'] = material_list
    return render(request, 'material/all_materials.html', context)

def view_material(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    material = Material.objects.get(id=id)
    context['material'] = material

    context['material_prices'] = get_price_history(material.id)
    context['material_price'] = get_current_price(material.id)
    return render(request, 'material/view_material.html', context)
