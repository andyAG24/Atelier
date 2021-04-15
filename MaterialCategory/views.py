from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _
from Material.models import Material
from .models import MaterialCategory
from MaterialPrice.views import get_material_with_price
from .forms import MaterialCategoryForm

@login_required(login_url='auth')
def all_categories(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name
    context['categories'] = get_categories()
    return render(request, 'material/category/all_categories.html', context)

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
    context['category'] = MaterialCategory.objects.get(id=id)
    context['category_materials'] = get_category_materials(id)
    return render(request, 'material/category/view_category.html', context)

def get_category_materials(category_id):
    category = MaterialCategory.objects.get(id=category_id)
    materials = Material.objects.filter(id_category=category_id)

    materials_with_price = []
    for material in materials:
        materials_with_price.append(get_material_with_price(material.id))

    return materials_with_price

@login_required(login_url='auth')
def add_category(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    error = ''
    if request.method == 'POST':
        category_form = MaterialCategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('all_categories')
        else:
            error = _('Form is invalid')

    category_form = MaterialCategoryForm()
    context['form'] = category_form
    context['error'] = error

    return render(request, 'material/category/add_category.html', context)

@login_required(login_url='auth')
def delete_category(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    MaterialCategory.objects.filter(id=id).delete()
    return redirect('all_categories')

class EditMaterialCategoryView(UpdateView):
    model = MaterialCategory
    template_name = 'material/category/add_category.html'
    form_class = MaterialCategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_group'] = self.request.user.groups.all()[0].name
        return context
