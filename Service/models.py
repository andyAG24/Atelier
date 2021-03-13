from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

class Service(models.Model):
    name = models.CharField(db_column='Name', 
                            verbose_name=_('Name'),
                            max_length=50)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', 
                                verbose_name=_('Price'),
                                max_digits=19, 
                                decimal_places=2)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', 
                               verbose_name=_('Comment'),
                               max_length=255, 
                               blank=True, 
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.name
