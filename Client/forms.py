from django import forms
from django.forms import ModelForm, TextInput, NumberInput
from .models import Client
from django.utils.translation import ugettext_lazy as _

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ivan')
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ivanov'),
            }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'type': 'tel',
                'pattern': '7[0-9]{10}',
                'placeholder': '79001234567',
            }),
            'height': NumberInput(attrs={
                'class': 'form-control',
            }),
            'chest_girth': NumberInput(attrs={
                'class': 'form-control',
            }),
            'chest_height': NumberInput(attrs={
                'class': 'form-control',
            }),
            'waist_girth': NumberInput(attrs={
                'class': 'form-control',
            }),
            'hip_girth': NumberInput(attrs={
                'class': 'form-control',
            }),
            'neck_girth': NumberInput(attrs={
                'class': 'form-control',
            }),
            'shoulder_girth': NumberInput(attrs={
                'class': 'form-control',
            }),
            'hand_girth': NumberInput(attrs={
                'class': 'form-control',
            }),
            'hand_length': NumberInput(attrs={
                'class': 'form-control',
            }),
            'back_width': NumberInput(attrs={
                'class': 'form-control',
            }),
            'length_waist_floor': NumberInput(attrs={
                'class': 'form-control',
            }),
        }
