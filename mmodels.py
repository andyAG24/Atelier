# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    first_name = models.CharField(db_column='First name', max_length=50)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_name = models.CharField(db_column='Last name', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    id = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column='id', primary_key=True)
    employee_type = models.CharField(db_column='Employee type', max_length=9)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    work_xp = models.IntegerField(db_column='Work XP', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeServices(models.Model):
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_Employee', blank=True, null=True)  # Field name made lowercase.
    id_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_Service', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee services'


class Fitting(models.Model):
    index_number = models.IntegerField(db_column='Index number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id_order = models.ForeignKey('Order', models.DO_NOTHING, db_column='id_Order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fitting'


class Material(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    vendor_code = models.CharField(db_column='Vendor code', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_category = models.ForeignKey('MaterialCategory', models.DO_NOTHING, db_column='id_Category', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material'


class MaterialCategory(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material category'


class MaterialPrice(models.Model):
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    modification_date = models.DateTimeField(db_column='Modification date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='id_Material', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material price'


class Order(models.Model):
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    payment_status = models.CharField(db_column='Payment status', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prepayment = models.DecimalField(db_column='Prepayment', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateTimeField(db_column='Start date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    end_date = models.DateTimeField(db_column='End date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='id_Client', blank=True, null=True)  # Field name made lowercase.
    id_employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='id_Employee', blank=True, null=True)  # Field name made lowercase.
    labour_intensity = models.CharField(db_column='Labour intensity', max_length=9)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urgency = models.CharField(db_column='Urgency', max_length=9)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    id_service = models.ForeignKey('Service', models.DO_NOTHING, db_column='id_Service', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class OrderMaterials(models.Model):
    id_order = models.ForeignKey(Order, models.DO_NOTHING, db_column='id_Order', blank=True, null=True)  # Field name made lowercase.
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='id_Material', blank=True, null=True)  # Field name made lowercase.
    material_quantity = models.IntegerField(db_column='Material quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'order materials'


class Service(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'


class ServicePrice(models.Model):
    price = models.DecimalField(db_column='Price', max_digits=19, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    modification_date = models.DateTimeField(db_column='Modification date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    id_service = models.ForeignKey(Service, models.DO_NOTHING, db_column='id_Service', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service price'
