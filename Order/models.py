from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from Client.models import Client
from Employee.models import Employee
from Material.models import Material
from Service.models import Service

class Order(models.Model):
    STATUS_CREATED = 'Created'
    STATUS_CANCELLED = 'Cancelled'
    STATUS_IN_PROGRESS = 'In progress'
    STATUS_COMPLETED = 'Completed'
    STATUS_PASSED_TO_CLIENT = 'Passed to the client'
    STATUS_RETURNED_FOR_REWORK = 'Returned for rework'
    STATUS_FIELD_CHOICES = (
        (STATUS_CREATED, _('Created')),
        (STATUS_CANCELLED, _('Cancelled')),
        (STATUS_IN_PROGRESS, _('In progress')),
        (STATUS_COMPLETED, _('Completed')),
        (STATUS_PASSED_TO_CLIENT, _('Passed to the client')),
        (STATUS_RETURNED_FOR_REWORK, _('Returned for rework')),
    )

    PRIORITY_LOW = 'Low'
    PRIORITY_MEDIUM = 'Medium'
    PRIOTITY_HIGH = 'High'
    PRIOTITY_VERY_HIGH = 'Very high'
    PRIORITY_FIELD_CHOICES = (
        (PRIORITY_LOW, _('Low')),
        (PRIORITY_MEDIUM, _('Medium')),
        (PRIOTITY_HIGH, _('High')),
        (PRIOTITY_VERY_HIGH, _('Very high')),
    )

    LEAD_TIME_SHORT = 'Short'
    LEAD_TIME_MEDIUM = 'Medium'
    LEAD_TIME_LONG = 'Long'
    LEAD_TIME_VERY_LONG = 'Very long'
    LEAD_TIME_FIELD_CHOICES = (
        (LEAD_TIME_SHORT, _('Short (1-3 days)')),
        (LEAD_TIME_MEDIUM, _('Medium (4-6 days)')),
        (LEAD_TIME_LONG, _('Long (7-9 days)')),
        (LEAD_TIME_VERY_LONG, _('Very long (10+ days)')),
    )

    status = models.CharField(db_column='Status',
                              verbose_name=_('Status'),
                              max_length=255, 
                              blank=True, 
                              null=True,
                              choices=STATUS_FIELD_CHOICES,
                              default=STATUS_CREATED)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', 
                               verbose_name=_('Cost'),
                               max_digits=19, 
                               decimal_places=2, 
                               blank=True, 
                               null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start date', 
                                      verbose_name=_('Start date'),
                                      blank=True, 
                                      null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateTimeField(db_column='End date', 
                                    verbose_name=_('End date'),
                                    blank=True, 
                                    null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_client = models.ForeignKey(Client, 
                                  models.DO_NOTHING, 
                                  db_column='id_Client', 
                                  verbose_name=_('Client'), 
                                  blank=True, 
                                  null=True)  # Field name made lowercase.
    id_employee = models.ForeignKey(Employee, 
                                    models.DO_NOTHING, 
                                    db_column='id_Employee', 
                                    verbose_name=_('Employee'), 
                                    blank=True, 
                                    null=True)  # Field name made lowercase.
    lead_time = models.CharField(db_column='Lead time', 
                                 verbose_name=_('Lead time'),
                                 max_length=45, 
                                 choices=LEAD_TIME_FIELD_CHOICES,
                                 default=LEAD_TIME_SHORT,
                                 blank=True, 
                                 null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    priority = models.IntegerField(db_column='Priority', 
                                   verbose_name=_('Priority'),
                                   choices=PRIORITY_FIELD_CHOICES,
                                   default=PRIORITY_LOW,
                                   blank=True, 
                                   null=True)  # Field name made lowercase.
    materials = models.ManyToManyField(Material, through='OrderMaterials')
    services = models.ManyToManyField(Service, through='OrderServices')
    comment = models.TextField(db_column='Comment', 
                               verbose_name=_('Comment'),
                               max_length=255, 
                               blank=True, 
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return _('%s, Order #%s, created on: %s, sum: %s') % (self.status, self.id, self.start_date, self.cost)

class OrderMaterials(models.Model):
    id_order = models.ForeignKey(Order, 
                                 models.CASCADE, 
                                 db_column='id_Order', 
                                 verbose_name=_('Order'),
                                 blank=True, 
                                 null=True)  # Field name made lowercase.
    id_material = models.ForeignKey(Material, 
                                    models.CASCADE, 
                                    db_column='id_Material', 
                                    verbose_name=_('Material'), 
                                    blank=True, 
                                    null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order materials'
        verbose_name_plural = _('Order materials')

class OrderMaterialsInline(admin.TabularInline):
    model = OrderMaterials
    extra = 1

class OrderServices(models.Model):
    id_order = models.ForeignKey(Order, 
                                 models.CASCADE, 
                                 db_column='id_Order', 
                                 verbose_name=_('Order'),
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
        db_table = 'order services'
        verbose_name_plural = _('Order services')

class OrderServicesInline(admin.TabularInline):
    model = OrderServices
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderMaterialsInline, OrderServicesInline,)
    