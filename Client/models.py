from django.db import models

class Client(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    chest_girth = models.IntegerField(db_column='Chest girth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chest_height = models.IntegerField(db_column='Chest height', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    waist_girth = models.IntegerField(db_column='Waist girth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hip_girth = models.IntegerField(db_column='Hip girth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    neck_girth = models.IntegerField(db_column='Neck girth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shoulder_girth = models.IntegerField(db_column='Shoulder girth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hand_girth = models.IntegerField(db_column='Hand girth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hand_length = models.IntegerField(db_column='Hand length', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    back_width = models.IntegerField(db_column='Back width', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    length_waist_floor = models.IntegerField(db_column='Length waist-floor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name) 