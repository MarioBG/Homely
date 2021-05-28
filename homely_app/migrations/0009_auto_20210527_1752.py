# Generated by Django 2.2 on 2021-05-27 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homely_app', '0008_auto_20210524_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasableitem',
            name='notes',
            field=models.CharField(blank=True, max_length=512, verbose_name='Notas'),
        ),
        migrations.AddField(
            model_name='purchasableitemvariation',
            name='sourceItem',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='homely_app.PurchasableItem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchasableitemvariation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='relItem', to='homely_app.PurchasableItem'),
        ),
    ]
