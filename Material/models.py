from django.db import models
from MaterialCategory.models import MaterialCategory

class Material(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    id_category = models.ForeignKey(MaterialCategory, models.DO_NOTHING, db_column='id_Category', verbose_name='Category', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', verbose_name='Price (per meter)', max_digits=19, decimal_places=2)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', verbose_name='Balance (meters)', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'material'

    def __str__(self):
        return '{0} {1}, {2} RUB (bal: {3} m)'.format(self.name, self.color, self.price, self.balance)
