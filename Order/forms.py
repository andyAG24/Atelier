from flatpickr import DateTimePickerInput

from django import forms
from django.db import models
from django.forms import ModelForm, NumberInput, Textarea, Select
from django.utils.translation import ugettext_lazy as _
from .models import Order
from Service.models import Service
from Client.models import Client
from Employee.models import Employee

class OrderForm(ModelForm):
    class OrderStatus(models.TextChoices):
        CREATED = 'Created', _('Created')
        CANCELLED = 'Cancelled', _('Cancelled')
        IN_PROGRESS = 'In progress', _('In progress')
        COMPLETED = 'Completed', _('Completed')
        PASSED_TO_CLIENT = 'Passed to the client', _('Passed to the client')
        RETURNED_FOR_REWORK = 'Returned for rework', _('Returned for rework')

    class LabourIntensity(models.TextChoices):
        LOW = 'Low', _('1-3 days')
        MEDIUM = 'Medium', _('4-6 days')
        HIGH = 'High', _('7-9 days')
        VERY_HIGH = 'Very high', _('10+ days')

    class Urgency(models.TextChoices):
        LOW = 'Low', _('Low urgency')
        MEDIUM = 'Medium', _('Medium urgency')
        HIGH = 'High', _('High urgency')
        VERY_HIGH = 'Very high', _('Very high urgency')

    class PaymentStatus(models.TextChoices):
        PENDING = 'Pending payment', _('Pending payment')
        PREPAYMENT_MADE = 'Prepayment made', _('Prepayment made')
        PAID = 'Paid', _('Paid')

    id_service = forms.ModelChoiceField(queryset=Service.objects.all(),
                                         widget=Select(attrs={
                                             'class': 'custom-select',
                                         }))
    id_client = forms.ModelChoiceField(queryset=Client.objects.all(),
                                         widget=Select(attrs={
                                             'class': 'custom-select',
                                         }))
    id_employee = forms.ModelChoiceField(queryset=Employee.objects.filter(employee_type='Sewer'),
                                         widget=Select(attrs={
                                             'class': 'custom-select',
                                         }))
    labour_intensity = forms.ChoiceField(choices=LabourIntensity.choices,
                                         widget=Select(attrs={
                                             'class': 'custom-select',
                                         }))
    
    # Для настройки. Обычно должно автоматически настраиваться 
    urgency = forms.ChoiceField(choices=Urgency.choices,
                                widget=Select(attrs={
                                    'class': 'custom-select',
                                    'required': True,
                                    'disabled': True
                                }))
    # Для настройки. Обычно заказ должен создаваться уже со статусом "создан"
    status = forms.ChoiceField(choices=OrderStatus.choices,
                               initial=OrderStatus.CREATED,
                               widget=Select(attrs={
                                   'class': 'custom-select',
                                   'hidden': True
                               }))

    payment_status = forms.ChoiceField(choices=PaymentStatus.choices,
                                         widget=Select(attrs={
                                             'class': 'custom-select',
                                         }))
    target_completion_date = forms.DateTimeField(widget=DateTimePickerInput(
        attrs={
            "class": "form-control",
        },
        options={
            "minDate": "today",
        }
    ))

    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'prepayment': NumberInput(attrs={
                'class': 'form-control',
            }),
            'cost': NumberInput(attrs={
                'class': 'form-control',
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
