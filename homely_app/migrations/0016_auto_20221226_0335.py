# Generated by Django 2.2.24 on 2022-12-26 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homely_app', '0015_recipe_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de etiqueta')),
                ('key', models.CharField(max_length=16, verbose_name='Valor de etiqueta')),
            ],
        ),
        migrations.AddField(
            model_name='movement',
            name='monthlyRecurrence',
            field=models.BooleanField(default=False, verbose_name='Recurrencia mensual'),
        ),
        migrations.AddField(
            model_name='movement',
            name='yearlyRecurrence',
            field=models.BooleanField(default=False, verbose_name='Recurrencia anual'),
        ),
        migrations.CreateModel(
            name='Mortgage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('euribor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Euribor')),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Añadido a euribor')),
                ('starting_capital', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Capital por pagar')),
                ('duration_months', models.IntegerField(verbose_name='Meses del préstamo')),
                ('fixed_months', models.IntegerField(verbose_name='Meses iniciales a interés fijo')),
                ('fixedterm_interest', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Interés del plazo a término fijo')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homely_app.Flat')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='tagged_item', to='homely_app.Tag', verbose_name='Tags'),
        ),
    ]
