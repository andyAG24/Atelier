from django.db import models
from django.utils.translation import ugettext_lazy as _
from MaterialCategory.models import MaterialCategory

class Material(models.Model):
    name = models.CharField(db_column='Name', 
                            verbose_name=_('Name'),
                            max_length=50)  # Field name made lowercase.
    vendor_code = models.CharField(db_column='Vendor code', 
                                   verbose_name=_('Vendor code'),
                                   max_length=45, 
                                   blank=True, 
                                   null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_category = models.ForeignKey(MaterialCategory, 
                                    models.DO_NOTHING, 
                                    db_column='id_Category', 
                                    verbose_name=_('Category'), 
                                    blank=True, 
                                    null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment',
                               verbose_name=_('Comment'),  
                               blank=True, 
                               null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', 
                                  verbose_name=_('Balance (meters)'), 
                                  blank=True, 
                                  null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', 
                             verbose_name=_('Color'),
                             max_length=255, 
                             blank=True, 
                             null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'material'
        verbose_name = _('Material')
        verbose_name_plural = _('Materials')

    def __str__(self):
        return _('%s %s (balance: %s m)') % (self.name, self.color, self.balance)
