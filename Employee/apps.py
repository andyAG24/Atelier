from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class EmployeeConfig(AppConfig):
    name = 'Employee'
    verbose_name = _('Employee')
