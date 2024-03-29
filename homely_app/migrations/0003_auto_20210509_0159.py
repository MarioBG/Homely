# Generated by Django 2.2 on 2021-05-08 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homely_app', '0002_auto_20210506_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorCodename', models.CharField(max_length=64, verbose_name='Código en el SVG del plano')),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorplan', models.FileField(upload_to='floorplans/', verbose_name='Plano de planta')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4096)),
                ('timestamp', models.DateTimeField()),
                ('mine', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipePics/%Y%m%d-%H%M/'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piso', to='homely_app.Flat')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other', to='homely_app.UserProfile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='homely_app.UserProfile')),
            ],
        ),
    ]
