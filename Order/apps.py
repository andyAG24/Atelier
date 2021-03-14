from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class OrderConfig(AppConfig):
    name = 'Order'
    verbose_name = _('Order')
