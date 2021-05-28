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


class Room(models.Model):
    name = models.CharField(verbose_name=_("Nombre de habitación"), max_length=200, blank=False)
    image = models.ImageField(upload_to='rooms/', blank=True)

    def __str__(self):
        return self.name


class StorageSpace(models.Model):
    parentStorageSpace = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Nombre de espacio de almacenaje"), max_length=200, blank=False)
    image = models.ImageField(upload_to='storageSpaces/', blank=True)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(models.Model):
    TYPES = [('liq_edible', 'Líquido comestible'), ('liq_cleaning', 'Líquido de limpieza'), ('sol_unit_edible', 'Sólido comestible por unidades'),
               ('sol_weight_edible', 'Sólido comestible por peso'), ('sol_cleaning', 'Sólidos para limpieza'), ('supply', 'Suministro'),
               ('consumable', 'Consumible genérico'), ('tool', 'Herramienta'), ('furniture', 'Mobiliario'), ('dishware', 'Vajilla'),
               ('electronics', 'Electrónica'), ('other', 'Otros')]
    name = models.CharField(verbose_name=_("Nombre de objeto"), max_length=200)
    type = models.CharField(verbose_name=_("Tipo de objeto"), max_length=60, choices=TYPES, default='other')
    image = models.ImageField(upload_to='items/', blank=True)

    def __str__(self):
        return self.name+" ("+self.type+")"


class PurchasableItem(models.Model):
    name = models.CharField(verbose_name=_("Nombre de objeto"), max_length=200)
    amount = models.DecimalField(verbose_name=_("Cantidad"), decimal_places=3, max_digits=9, default=0)
    price = models.DecimalField(verbose_name=_("Precio"), decimal_places=2, max_digits=10)
    remaining = models.DecimalField(verbose_name=_("Cantidad restante"), decimal_places=3, max_digits=9, default=0)
    parentItem = models.ForeignKey(to=Item, on_delete=models.CASCADE, related_name="parentItem")
    isTemplate = models.BooleanField(verbose_name=_("¿Es una plantilla?"), null=False)
    isWishlist = models.BooleanField(verbose_name=_("¿Es un elemento de lista de deseos?"), null=False)
    notes = models.CharField(max_length=512, blank=True, verbose_name=_("Notas"))
    storageSpace = models.ForeignKey(verbose_name=_("Lugar de almacenaje"), to=Room, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='purchasableItems/', blank=True)
    barCode = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name+" ("+self.type+")"


class PurchasableItemVariation(models.Model):
    TYPES = [('PURCHASE', "Purchase"), ('CONSUMPTION', 'Consumption'), ('THROW_AWAY', 'Throw away'), ('REPLACEMENT', 'Replacement'),
             ('REFILLMENT', 'Refillment')]
    date = models.DateTimeField(verbose_name=_("Fecha de transacción"), null=False)
    item = models.ForeignKey(to=PurchasableItem, on_delete=models.PROTECT, related_name="relItem")
    sourceItem = models.ForeignKey(to=PurchasableItem, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_("Cantidad"))
    type = models.CharField(choices=TYPES, max_length=32)

    def __str__(self):
        return self.type+" ("+self.item.name+"), "+self.amount


class SmartDevice(models.Model):
    name = models.CharField(verbose_name=_("Nombre de objeto inteligente"), max_length=200, blank=False)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='smartDevices/', blank=True)

    def __str__(self):
        return self.name


class SmartMethod(models.Model):
    name = models.CharField(verbose_name=_("Nombre de método"), max_length=200, blank=False)
    object = models.ForeignKey(to=SmartDevice, on_delete=models.CASCADE)


class Movement(models.Model):
    name = models.CharField(verbose_name=_("Nombre de movimiento"), max_length=200, blank=False)
    date = models.DateTimeField(verbose_name=_("Fecha"), null=False)
    recurrence = models.IntegerField(verbose_name=_("Días de recurrencia"), blank=True)
    amount = models.DecimalField(verbose_name=_("Cantidad"), decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name+" ("+self.amount+"€)"


class Recipe(models.Model):
    name = models.CharField(verbose_name=_("Nombre de receta"), max_length=200, blank=False)
    image = models.ImageField(upload_to='recipePics/%Y%m%d-%H%M/', blank=True)
    process = MartorField(verbose_name="Pasos de la receta", blank=True)

    def __str__(self):
        return self.name


class RecipeRequirement(models.Model):
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name=_("Cantidad"), decimal_places=2, max_digits=10)

    def __str__(self):
        return self.item.name+" ("+str(self.amount)+")"



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