# Generated by Django 3.1.2 on 2021-03-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=255, null=True)),
                ('cost', models.DecimalField(blank=True, db_column='Cost', decimal_places=2, max_digits=19, null=True)),
                ('start_date', models.DateTimeField(blank=True, db_column='Start date', null=True)),
                ('end_date', models.DateTimeField(blank=True, db_column='End date', null=True)),
                ('lead_time', models.IntegerField(blank=True, db_column='Lead time', null=True)),
                ('priority', models.IntegerField(blank=True, db_column='Priority', null=True)),
                ('comment', models.CharField(blank=True, db_column='Comment', max_length=255, null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
    ]
