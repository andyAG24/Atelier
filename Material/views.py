
from django.http import Http404
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _
from MaterialPrice.views import get_current_price, get_price_history
from MaterialCategory.models import MaterialCategory
from MaterialPrice.models import MaterialPrice
from .models import Material
from .forms import MaterialForm, MaterialPriceForm

@login_required(login_url='auth')
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

@login_required(login_url='auth')
def view_material(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    material = Material.objects.get(id=id)
    context['material'] = material

    context['material_prices'] = get_price_history(material.id)
    context['material_price'] = get_current_price(material.id)
    return render(request, 'material/view_material.html', context)

@login_required(login_url='auth')
def add_material(request):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    error = ''
    if request.method == 'POST':
        material_form = MaterialForm(request.POST)
        material_price_form = MaterialPriceForm(request.POST)
        if material_form.is_valid() and material_price_form.is_valid():
            material = material_form.save()
            
            material_price = material_price_form.save(commit=False)
            material_price.id_material = Material.objects.get(id=material.pk)
            material_price.modification_date = datetime.now()
            material_price.save()

            return redirect('all_materials')
        else:
            error = _('Form is invalid')

    material_form = MaterialForm()
    material_price_form = MaterialPriceForm()
    context['form'] = material_form
    context['material_price_form'] = material_price_form
    context['error'] = error

    return render(request, 'material/add_material.html', context)

@login_required(login_url='auth')
def delete_material(request, id):
    context = {}
    context['user_group'] = request.user.groups.all()[0].name

    Material.objects.filter(id=id).delete()
    return redirect('all_materials')

class EditMaterialView(UpdateView):
    model = Material
    template_name = 'material/add_material.html'
    form_class = MaterialForm
    second_form_class = MaterialPriceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_group'] = self.request.user.groups.all()[0].name

        if 'material_price_form' not in context:
            current_price = MaterialPrice.objects.filter(id_material=self.kwargs['pk']).order_by('-modification_date')[0]

            context['material_price_form'] = MaterialPriceForm(instance=current_price)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super(EditMaterialView, self).get_context_data(**kwargs)

        if 'form' in context:
            form = MaterialForm(request.POST, instance=self.object)
            if form.is_valid():
                form.save()
            else:
                context['form'] = form

        current_price = MaterialPrice.objects.filter(id_material=self.object.id).order_by('-modification_date')[0]
        if 'price' in request.POST:
            if request.POST['price'] != '':
                new_price = float(request.POST['price'])
            else:
                new_price = float(0)
            if new_price != current_price.price:
                new_material_price = MaterialPrice(id_material=self.object, price=new_price, modification_date=datetime.now())
                new_material_price.save()
        
        return redirect(self.object.get_absolute_url())
