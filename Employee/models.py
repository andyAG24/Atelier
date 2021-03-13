from django.db import models
from django.contrib import admin
from Service.models import Service

class Employee(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=255)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    work_xp = models.IntegerField(db_column='Work XP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    services = models.ManyToManyField(Service, through='EmployeeServices')

    class Meta:
        managed = False
        db_table = 'employee'

    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name) 

class EmployeeServices(models.Model):
    id_employee = models.ForeignKey(Employee, models.CASCADE, db_column='id_Employee', blank=True, null=True)  # Field name made lowercase.
    id_service = models.ForeignKey(Service, models.CASCADE, db_column='id_Service', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee services'
        verbose_name_plural = 'Employee services'

class EmployeeServicesInline(admin.TabularInline):
    model = EmployeeServices
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    inlines = (EmployeeServicesInline,)
