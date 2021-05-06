from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
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
from mptt.models import MPTTModel
import mptt
from django.db.models import F
from treewidget.fields import TreeForeignKey

# Create your models here.
# System objects

class Item(models.Model):
    TYPES = [('liq_edible', 'Líquido comestible'), ('liq_cleaning', 'Líquido de limpieza'), ('sol_unit_edible', 'Sólido comestible por unidades'),
               ('sol_weight_edible', 'Sólido comestible por peso'), ('sol_cleaning', 'Sólidos para limpieza'), ('supply', 'Suministro'),
               ('consumable', 'Consumible genérico'), ('tool', 'Herramienta'), ('furniture', 'Mobiliario')]
    name = models.CharField(verbose_name=_("Nombre de objeto"), max_length=200)

class Room(models.Model):
    name = models.CharField(verbose_name=_("Nombre de habitación"), max_length=200)

class StorageSpace(models.Model):
    name = models.CharField(verbose_name=_("Nombre de espacio de almacenaje"), max_length=200)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)