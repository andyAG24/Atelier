from django.db import models
from Service.models import Service
from django.utils.translation import ugettext_lazy as _

class ServicePrice(models.Model):
    id_service = models.ForeignKey(Service, 
                                   models.DO_NOTHING, 
                                   db_column='id_Service', 
                                   verbose_name=_('Service'),
                                   blank=True, 
                                   null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', 
                                verbose_name=_('Price'),
                                max_digits=19, 
                                decimal_places=2, 
                                blank=True, 
                                null=True)  # Field name made lowercase.
    modification_date = models.DateTimeField(db_column='Modification date',
                                             verbose_name=_('Modification date'), 
                                             blank=True, 
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'service price'
        verbose_name = _('Service price')
        verbose_name_plural = _('Services prices')

    def __str__(self):
        return f"{self.id_service.name}, {self.modification_date}, {self.price}"