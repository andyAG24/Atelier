from django.db import models
from django.utils.translation import ugettext_lazy as _
from Order.models import Order

class Fitting(models.Model):
    class FittingStatus(models.TextChoices):
        CREATED = 'Created', _('Created')
        CLIENT_IS_CALLED = 'The client is called for fitting', _('The client is called for fitting')
        PRODUCT_FITS_IN_SIZE = 'The product fits in size', _('The product fits in size')
        THERE_ARE_FLAWS = 'There are flaws', _('There are flaws') 

    id_order = models.ForeignKey(Order,
                                 models.CASCADE,
                                 db_column='id_Order',
                                 verbose_name=_('Order'))
    index_number = models.IntegerField(db_column='Index number',
                                       verbose_name=_('Index number'),
                                       blank=True,
                                       null=True)
    date = models.DateTimeField(db_column='Date',
                                verbose_name=_('Date'),
                                blank=True,
                                null=True)
    status = models.CharField(db_column='Status',
                              verbose_name=_('Status'),
                              max_length=32,
                              choices=FittingStatus.choices,
                              default=FittingStatus.CREATED)

    class Meta:
        managed = False
        db_table = 'fitting'
        verbose_name = _('Fitting')
        verbose_name_plural = _('Fittings')
        