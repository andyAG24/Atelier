from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ClientConfig(AppConfig):
    name = 'Client'
    verbose_name = _('Client')
