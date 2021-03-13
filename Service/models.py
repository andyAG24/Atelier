from django.db import models
from django.contrib import admin
# Create your models here.

class Service(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=2)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'

    def __str__(self):
        return self.name
