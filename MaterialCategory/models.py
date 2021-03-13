from django.db import models

class MaterialCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material category'
        verbose_name_plural = 'material categories'

    def __str__(self):
        return self.name