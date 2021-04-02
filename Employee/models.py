from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from Service.models import Service

class Employee(models.Model):
    class EmployeeType(models.TextChoices):
        SEWER = 'SEWER', _('Sewer')
        MANAGER = 'MANAGER', _('Manager')
        UNDEFINED = 'UNDEFINED', _('Undefined')

    id = models.OneToOneField(User,
                              models.CASCADE,
                              db_column='id',
                              verbose_name=_('User'),
                              primary_key=True)
    employee_type = models.CharField(db_column='Employee type',
                                     verbose_name=_('Employee type'),
                                     max_length=9,
                                     choices=EmployeeType.choices,
                                     default=EmployeeType.UNDEFINED)
    phone = models.CharField(db_column='Phone',
                             verbose_name=_('Phone'),
                             max_length=255)
    work_xp = models.IntegerField(db_column='Work XP',
                                  verbose_name=_('Work XP'),
                                  blank=True,
                                  null=True)

    class Meta:
        managed = False
        db_table = 'employee'
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def is_manager(self):
        groups = self.id.groups.all()
        return groups.filter(name='Managers').exists()

    def is_sewer(self):
        groups = self.id.groups.all()
        return groups.filter(name='Sewers').exists()

    def __str__(self):
        if self.id.first_name and self.id.last_name:
            return '{0} {1}'.format(self.id.last_name, self.id.first_name)
        elif self.id.last_name:
            return '{0} ({1})'.format(self.id.last_name, self.id.username)
        else:
            return '{0}'.format(self.id.username)

class EmployeeServices(models.Model):
    id_employee = models.ForeignKey(Employee,
                                    models.CASCADE,
                                    db_column='id_Employee',
                                    verbose_name=_('Employee'),
                                    blank=True,
                                    null=True)
    id_service = models.ForeignKey(Service,
                                   models.CASCADE,
                                   db_column='id_Service',
                                   # verbose_name=_('Service'),
                                   blank=True,
                                   null=True)

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
