from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from Service.models import Service

class Employee(models.Model):
    name = models.CharField(db_column='Name', 
                            verbose_name=_('Name'),
                            max_length=50)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', 
                               verbose_name=_('Surname'),
                               max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', 
                             verbose_name=_('Phone'),
                             max_length=255)  # Field name made lowercase.
    work_xp = models.IntegerField(db_column='Work XP', 
                                  verbose_name=_('Work XP'),
                                  blank=True, 
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    services = models.ManyToManyField(Service, through='EmployeeServices')

    class Meta:
        managed = False
        db_table = 'employee'
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name) 

class EmployeeServices(models.Model):
    id_employee = models.ForeignKey(Employee, 
                                    models.CASCADE, 
                                    db_column='id_Employee', 
                                    verbose_name=_('Employee'),
                                    blank=True, 
                                    null=True)  # Field name made lowercase.
    id_service = models.ForeignKey(Service, 
                                   models.CASCADE, 
                                   db_column='id_Service', 
                                   verbose_name=_('Service'),
                                   blank=True, 
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee services'
        verbose_name = _('Employee services')
        verbose_name_plural = _('Employee services')

class EmployeeServicesInline(admin.TabularInline):
    model = EmployeeServices
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeServicesInline,)
