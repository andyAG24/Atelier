from django.db import models
from django.contrib import admin
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
        (STATUS_CREATED, 'Created'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_PASSED_TO_CLIENT, 'Passed to the client'),
        (STATUS_RETURNED_FOR_REWORK, 'Returned for rework'),
    )

    status = models.CharField(db_column='Status', 
                              max_length=255, 
                              blank=True, 
                              null=True,
                              choices=STATUS_FIELD_CHOICES,
                              default=STATUS_CREATED)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateTimeField(db_column='End date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_Client', verbose_name='Client', blank=True, null=True)  # Field name made lowercase.
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_Employee', verbose_name='Employee', blank=True, null=True)  # Field name made lowercase.
    lead_time = models.IntegerField(db_column='Lead time', verbose_name='Lead time (days)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.
    materials = models.ManyToManyField(Material, through='OrderMaterials')
    services = models.ManyToManyField(Service, through='OrderServices')
    comment = models.TextField(db_column='Comment', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'

    def __str__(self):
        return '{0}, Order #{1}, created on: {2}, sum: {3}'.format(self.status, self.id, self.start_date, self.cost)

class OrderMaterials(models.Model):
    id_order = models.ForeignKey(Order, models.CASCADE, db_column='id_Order', blank=True, null=True)  # Field name made lowercase.
    id_material = models.ForeignKey(Material, models.CASCADE, db_column='id_Material', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order materials'
        verbose_name_plural = 'order materials'

class OrderMaterialsInline(admin.TabularInline):
    model = OrderMaterials
    extra = 1

class OrderServices(models.Model):
    id_order = models.ForeignKey(Order, models.CASCADE, db_column='id_Order', blank=True, null=True)  # Field name made lowercase.
    id_service = models.ForeignKey(Service, models.CASCADE, db_column='id_Service', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order services'
        verbose_name_plural = 'order services'

class OrderServicesInline(admin.TabularInline):
    model = OrderServices
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderMaterialsInline, OrderServicesInline,)
    