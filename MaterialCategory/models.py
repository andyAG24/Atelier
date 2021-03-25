from django.db import models
from django.utils.translation import ugettext_lazy as _

class MaterialCategory(models.Model):
    name = models.CharField(db_column='Name', 
                            verbose_name=_('Name'),
                            max_length=50)
    comment = models.TextField(db_column='Comment', 
                               verbose_name=_('Comment'),
                               blank=True, 
                               null=True)

    class Meta:
        managed = False
        db_table = 'material category'
        verbose_name = _('Material category')
        verbose_name_plural = _('Materials categories')

    def __str__(self):
        return self.name