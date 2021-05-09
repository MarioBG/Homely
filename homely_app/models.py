from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from martor.models import MartorField
import django.core.validators
from ordered_model.models import OrderedModel
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from mptt.models import MPTTModel
import mptt
from django.db.models import F
from treewidget.fields import TreeForeignKey

# Create your models here.
# System objects

class Item(models.Model):
    TYPES = [('liq_edible', 'Líquido comestible'), ('liq_cleaning', 'Líquido de limpieza'), ('sol_unit_edible', 'Sólido comestible por unidades'),
               ('sol_weight_edible', 'Sólido comestible por peso'), ('sol_cleaning', 'Sólidos para limpieza'), ('supply', 'Suministro'),
               ('consumable', 'Consumible genérico'), ('tool', 'Herramienta'), ('furniture', 'Mobiliario'), ('other', 'Otros')]
    name = models.CharField(verbose_name=_("Nombre de objeto"), max_length=200)
    type = models.CharField(verbose_name=_("Tipo de objeto"), max_length=60, choices=TYPES, default='other')
    amount = models.DecimalField(verbose_name=_("Cantidad"), decimal_places=3, max_digits=9, default=0)

class Room(models.Model):
    name = models.CharField(verbose_name=_("Nombre de habitación"), max_length=200, blank=False)

class StorageSpace(models.Model):
    name = models.CharField(verbose_name=_("Nombre de espacio de almacenaje"), max_length=200, blank=False)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

class SmartDevice(models.Model):
    name = models.CharField(verbose_name=_("Nombre de objeto inteligente"), max_length=200, blank=False)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

class SmartMethod(models.Model):
    name = models.CharField(verbose_name=_("Nombre de método"), max_length=200, blank=False)
    object = models.ForeignKey(to=SmartDevice, on_delete=models.CASCADE)

class Movement(models.Model):
    name = models.CharField(verbose_name=_("Nombre de movimiento"), max_length=200, blank=False)
    date = models.DateTimeField(verbose_name=_("Fecha"), null=False)
    recurrence = models.IntegerField(verbose_name=_("Días de recurrencia"), blank=True)
    amount = models.DecimalField(verbose_name=_("Cantidad"), decimal_places=2, max_digits=10)

class Recipe(models.Model):
    name = models.CharField(verbose_name=_("Nombre de receta"), max_length=200, blank=False)
    image = models.ImageField(upload_to='recipePics/%Y%m%d-%H%M/', blank=True)

class Floor(models.Model):
    floorplan = models.FileField(verbose_name="Plano de planta", upload_to="floorplans/", validators=[FileExtensionValidator(['svg'])])

class Flat(models.Model):
    floorCodename = models.CharField(verbose_name="Código en el SVG del plano", max_length=64)

class UserProfile(models.Model):
    user = models.OneToOneField(to=django.contrib.auth.models.User, related_name="user", on_delete=models.CASCADE)
    flat = models.ForeignKey(to=Flat, on_delete=models.CASCADE, related_name="piso")

class Conversation(models.Model):
    owner = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name="owner")
    other = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, related_name="other")

class Message(models.Model):
    text = models.CharField(blank=False, max_length=4096)
    timestamp = models.DateTimeField()
    mine = models.BooleanField()