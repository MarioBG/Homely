# Generated by Django 2.2 on 2021-05-16 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homely_app', '0004_auto_20210509_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='amount',
        ),
        migrations.CreateModel(
            name='PurchasableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre de objeto')),
                ('amount', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Cantidad')),
                ('remaining', models.DecimalField(decimal_places=3, default=0, max_digits=9, verbose_name='Cantidad restante')),
                ('isTemplate', models.BooleanField(verbose_name='¿Es una plantilla?')),
                ('parentItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentItem', to='homely_app.Item')),
            ],
        ),
    ]
