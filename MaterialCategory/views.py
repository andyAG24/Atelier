from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Material.models import Material
from MaterialCategory.models import MaterialCategory
from MaterialPrice.views import get_material_with_price

@login_required(login_url='auth')
def all_categories(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    context['categories'] = get_categories()
    return render(request, 'material/all_categories.html', context)

def get_categories():
    categories = MaterialCategory.objects.all()
    categories_list = []
    for category in categories:
        materials = Material.objects.filter(id_category=category.id)
        category_object = {
            'id': category.id,
            'name': category.name,
            'materials_count': materials.count()
        }
        categories_list.append(category_object)
    return categories_list

@login_required(login_url='auth')
def view_category(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    context['category_name'] = MaterialCategory.objects.get(id=id).name
    context['category_materials'] = get_category_materials(id)
    return render(request, 'material/view_category.html', context)

def get_category_materials(category_id):
    category = MaterialCategory.objects.get(id=category_id)
    materials = Material.objects.filter(id_category=category_id)

    materials_with_price = []
    for material in materials:
        materials_with_price.append(get_material_with_price(material.id))

    return materials_with_price
