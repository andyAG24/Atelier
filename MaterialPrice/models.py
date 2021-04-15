from django.db import models
from django.utils.translation import ugettext_lazy as _
from Material.models import Material

class MaterialPrice(models.Model):
    id_material = models.ForeignKey(Material,
                                    models.CASCADE,
                                    db_column='id_Material',
                                    verbose_name=_('Material'),
                                    blank=True,
                                    null=True)
    price = models.DecimalField(db_column='Price',
                                verbose_name=_('Price (per meter)'),
                                max_digits=19,
                                decimal_places=2,
                                blank=True,
                                null=True)
    modification_date = models.DateTimeField(db_column='Modification date',
                                             verbose_name=_('Modification date'),
                                             blank=True,
                                             null=True)

    class Meta:
        managed = False
        db_table = 'material price'
        verbose_name = _('Material price')
        verbose_name_plural = _('Materials prices')

    def __str__(self):
        return f"{self.id_material.name}, {self.modification_date}, {self.price}"

    def get_absolute_url(self):
        return f'/materials/view/{self.id}'
        