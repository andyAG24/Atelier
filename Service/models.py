from django.db import models
from django.utils.translation import ugettext_lazy as _

class Service(models.Model):
    name = models.CharField(db_column='Name',
                            verbose_name=_('Name'),
                            max_length=50)
    comment = models.TextField(db_column='Comment',
                               blank=True,
                               verbose_name=_('Commentary'),
                               null=True)

    class Meta:
        managed = False
        db_table = 'service'
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return f"{self.name}"
