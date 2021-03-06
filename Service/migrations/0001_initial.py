# Generated by Django 3.1.2 on 2021-03-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('price', models.DecimalField(db_column='Price', decimal_places=2, max_digits=19)),
                ('comment', models.CharField(blank=True, db_column='Comment', max_length=255, null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
    ]
