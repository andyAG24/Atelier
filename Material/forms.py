from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _
from MaterialCategory.models import MaterialCategory
from MaterialPrice.models import MaterialPrice
from .models import Material

class MaterialForm(ModelForm):
    id_category = forms.ModelChoiceField(queryset=MaterialCategory.objects.all(),
                                         widget=Select(attrs={
                                             'class': 'custom-select',
                                         }))

    class Meta:
        model = Material
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'vendor_code': TextInput(attrs={
                'class': 'form-control',
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'balance': NumberInput(attrs={
                'class': 'form-control',
            }),
            'color': TextInput(attrs={
                'class': 'form-control',
            }),
        }

class MaterialPriceForm(ModelForm):
    class Meta:
        model = MaterialPrice
        fields = ['id_material', 'price']
        widgets = {
            'price': NumberInput(attrs={
                'class': 'form-control',
            }),
        }
