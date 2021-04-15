from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _
from .models import MaterialCategory

class MaterialCategoryForm(ModelForm):
    class Meta:
        model = MaterialCategory
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }