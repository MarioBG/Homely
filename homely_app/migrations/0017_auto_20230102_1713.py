# Generated by Django 2.2.24 on 2023-01-02 16:13

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homely_app', '0016_auto_20221226_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Dificultad'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0), verbose_name='Tiempo de cocinado'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='healthiness',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Saludable'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('liq_edible', 'Líquido comestible'), ('liq_cleaning', 'Líquido de limpieza'), ('sol_unit_edible', 'Alimento sólido por unidades'), ('sol_weight_edible', 'Alimento sólido por peso'), ('sol_cleaning', 'Suministros de limpieza'), ('supply', 'Suministro'), ('consumable', 'Consumible genérico'), ('tool', 'Herramienta'), ('furniture', 'Mobiliario'), ('dishware', 'Vajilla'), ('electronics', 'Electrónica'), ('other', 'Otros')], default='other', max_length=60, verbose_name='Tipo de objeto'),
        ),
    ]
