from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from Client.models import Client
from Employee.models import Employee
from Material.models import Material
from Service.models import Service

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = 'Created', _('Created')
        CANCELLED = 'Cancelled', _('Cancelled')
        IN_PROGRESS = 'In progress', _('In progress')
        COMPLETED = 'Completed', _('Completed')
        PASSED_TO_CLIENT = 'Passed to the client', _('Passed to the client')
        RETURNED_FOR_REWORK = 'Returned for rework', _('Returned for rework')

    class Urgency(models.TextChoices):
        LOW = 'Low', _('Low urgency')
        MEDIUM = 'Medium', _('Medium urgency')
        HIGH = 'High', _('High urgency')
        VERY_HIGH = 'Very high', _('Very high urgency')

    class LabourIntensity(models.TextChoices):
        LOW = 'Low', _('1-3 days')
        MEDIUM = 'Medium', _('4-6 days')
        HIGH = 'High', _('7-9 days')
        VERY_HIGH = 'Very high', _('10+ days')

    class PaymentStatus(models.TextChoices):
        PENDING = 'Pending payment', _('Pending payment')
        PREPAYMENT_MADE = 'Prepayment made', _('Prepayment made')
        PAID = 'Paid', _('Paid')

    id_service = models.ForeignKey(Service,
                                   models.SET_NULL,
                                   db_column='id_Service',
                                   verbose_name=_('Service'),
                                   blank=True,
                                   null=True)
    status = models.CharField(db_column='Status',
                              verbose_name=_('Status'),
                              max_length=20,
                              choices=OrderStatus.choices,
                              default=OrderStatus.CREATED)
    payment_status = models.CharField(db_column='Payment status',
                                      verbose_name=_('Payment status'),
                                      max_length=15,
                                      choices=PaymentStatus.choices,
                                      blank=True,
                                      null=True)
    prepayment = models.DecimalField(db_column='Prepayment',
                                     verbose_name=_('Prepayment'),
                                     max_digits=19,
                                     decimal_places=2,
                                     blank=True,
                                     null=True)
    cost = models.DecimalField(db_column='Cost',
                               verbose_name=_('Cost'),
                               max_digits=19,
                               decimal_places=2,
                               blank=True,
                               null=True)
    start_date = models.DateTimeField(db_column='Start date',
                                      verbose_name=_('Start date'),
                                      blank=True,
                                      null=True)
    end_date = models.DateTimeField(db_column='End date',
                                    verbose_name=_('End date'),
                                    blank=True,
                                    null=True)
    id_client = models.ForeignKey(Client,
                                  models.SET_NULL,
                                  db_column='id_Client',
                                  verbose_name=_('Client'),
                                  blank=True,
                                  null=True)
    id_employee = models.ForeignKey(Employee,
                                    models.SET_NULL,
                                    db_column='id_Employee',
                                    verbose_name=_('Employee'),
                                    blank=True,
                                    null=True)
    labour_intensity = models.CharField(db_column='Labour intensity',
                                        verbose_name=_('Labour intensity'),
                                        max_length=9,
                                        choices=LabourIntensity.choices,
                                        default=LabourIntensity.LOW)
    urgency = models.CharField(db_column='Urgency',
                               verbose_name=_('Urgency'),
                               max_length=9,
                               choices=Urgency.choices,
                               default=Urgency.LOW)
    materials = models.ManyToManyField(Material, through='OrderMaterials')
    comment = models.TextField(db_column='Comment',
                               verbose_name=_('Comment'),
                               blank=True,
                               null=True)

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
                                 null=True)
    id_material = models.ForeignKey(Material,
                                    models.CASCADE,
                                    db_column='id_Material',
                                    verbose_name=_('Material'),
                                    blank=True,
                                    null=True)
    material_quantity = models.IntegerField(db_column='Material quantity',
                                            verbose_name=_('Material quantity'),
                                            blank=True,
                                            null=True)

    class Meta:
        managed = False
        db_table = 'order materials'
        verbose_name = _('Order material')
        verbose_name_plural = _('Order materials')

# @receiver(post_save, sender=Order)
# def update_material_quantity(sender, instance, **kwargs):
#     order_id = instance.id
#     order_materials = OrderMaterials.objects.filter(id_order=order_id)
#     for item in order_materials:
#         material = Material.objects.get(id=item.id_material.id)
#         material.balance -= item.material_quantity
#         material.save()
#         print(material)

class OrderMaterialsInline(admin.TabularInline):
    model = OrderMaterials
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderMaterialsInline,)
