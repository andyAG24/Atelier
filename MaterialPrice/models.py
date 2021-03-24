from django.db import models
from Material.models import Material
from django.utils.translation import ugettext_lazy as _

class MaterialPrice(models.Model):
    id_material = models.ForeignKey(Material, 
                                    models.DO_NOTHING, 
                                    db_column='id_Material',
                                    verbose_name=_('Material'), 
                                    blank=True, 
                                    null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', 
                                verbose_name=_('Price (per meter)'),
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
        db_table = 'material price'
        verbose_name = _('Material price')
        verbose_name_plural = _('Materials prices')
    
    def __str__(self):
        return f"{self.id_material.name}, {self.modification_date}, {self.price}"