# Generated by Django 2.2 on 2021-05-09 00:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homely_app', '0003_auto_20210509_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='floorplan',
            field=models.FileField(upload_to='floorplans/', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='Plano de planta'),
        ),
    ]
