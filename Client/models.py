from django.db import models
from django.utils.translation import ugettext_lazy as _

class Client(models.Model):
    name = models.CharField(db_column='Name', 
                            verbose_name=_('Name'),
                            max_length=50)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', 
                               verbose_name=_('Surname'),
                               max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone',
                             verbose_name=_('Phone'),
                             max_length=255)  # Field name made lowercase.
    height = models.IntegerField(db_column='Height', 
                                 verbose_name=_('Height'),
                                 blank=True, 
                                 null=True)  # Field name made lowercase.
    chest_girth = models.IntegerField(db_column='Chest girth', 
                                      verbose_name=_('Chest girth'),
                                      blank=True, 
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chest_height = models.IntegerField(db_column='Chest height', 
                                       verbose_name=_('Chest height'),
                                       blank=True, 
                                       null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    waist_girth = models.IntegerField(db_column='Waist girth', 
                                      verbose_name=_('Waist girth'),
                                      blank=True, 
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hip_girth = models.IntegerField(db_column='Hip girth', 
                                    verbose_name=_('Hip girth'),
                                    blank=True, 
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    neck_girth = models.IntegerField(db_column='Neck girth', 
                                     verbose_name=_('Neck girth'),
                                     blank=True, 
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shoulder_girth = models.IntegerField(db_column='Shoulder girth', 
                                         verbose_name=_('Shoulder girth'),
                                         blank=True, 
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hand_girth = models.IntegerField(db_column='Hand girth', 
                                     verbose_name=_('Hand girth'),
                                     blank=True, 
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hand_length = models.IntegerField(db_column='Hand length', 
                                      verbose_name=_('Hand length'),
                                      blank=True, 
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    back_width = models.IntegerField(db_column='Back width', 
                                     verbose_name=_('Back width'),
                                     blank=True, 
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    length_waist_floor = models.IntegerField(db_column='Length waist-floor', 
                                             verbose_name=_('Length waist-floor'),
                                             blank=True, 
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = _('Client')
        verbose_name_plural = _('Clients')

    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name) 