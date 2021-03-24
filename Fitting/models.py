from django.db import models
from django.utils.translation import ugettext_lazy as _
from Order.models import Order 

class Fitting(models.Model):
    id_order = models.ForeignKey(Order, 
                                 models.DO_NOTHING, 
                                 db_column='id_Order', 
                                 verbose_name=_('Order'),
                                 blank=True, 
                                 null=True)  # Field name made lowercase.
    index_number = models.IntegerField(db_column='Index number', 
                                       verbose_name=_('Index number'),
                                       blank=True, 
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date', 
                                verbose_name=_('Date'),
                                blank=True, 
                                null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', 
                              verbose_name=_('Status'),
                              max_length=255, 
                              blank=True, 
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fitting'
        verbose_name = _('Fitting')
        verbose_name_plural = _('Fittings')