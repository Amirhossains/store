from django.db import models
from django.utils.translation import gettext_lazy as _


class Edibles(models.Model):
    edibles = 1
    home_appliances = 2
    clothes = 3
    model_types = (
        (edibles, _('edibles')),
        (home_appliances, _('home_appliances')),
        (clothes, _('clothes')))
    model_type = models.PositiveIntegerField(verbose_name=_('model type'), choices=model_types, default=edibles)
    edible_type = models.CharField(verbose_name=_('edible type'), max_length=30)
    is_available = models.BooleanField(verbose_name=_('is available'), default=True)
    createdTime = models.DateTimeField(auto_now=True)
    updatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'edibles'
        verbose_name = _('edible')
        verbose_name_plural = _('edibles')

class EdiblesModel(models.Model):
    edible = models.ForeignKey(to=Edibles, related_name='edible', on_delete=models.CASCADE)
    mark = models.CharField(verbose_name=_('mark'), max_length=50)
    taste = models.CharField(verbose_name=_('taste'), max_length=30, blank=True)
    price = models.PositiveBigIntegerField(verbose_name=_('price'), default=1000)
    discount = models.CharField(verbose_name=_('discount'), blank=True, max_length=10)
    edibleImage = models.ImageField(verbose_name=_('edible image'), upload_to='edibles/', blank=True, null=True)
    Description = models.TextField(verbose_name=_('description'), max_length=300, blank=True, null=True)
    createdTime = models.DateTimeField(auto_now=True)
    updatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'edibles_models'
        verbose_name = _('edible model')
        verbose_name_plural = _("edibles model")

class HomeAppliances(models.Model):
    edibles = 1
    home_appliances = 2
    clothes = 3
    model_types = (
        (edibles, _('edibles')),
        (home_appliances, _('home_appliances')),
        (clothes, _('clothes')))
    model_type = models.PositiveIntegerField(verbose_name=_('model type'), choices=model_types, default=home_appliances)
    home_appliance_type = models.CharField(verbose_name=_('home appliances type'), max_length=30)
    is_available = models.BooleanField(verbose_name=_('is available'), default=True)
    createdTime = models.DateTimeField(auto_now=True)
    updatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'home_appliances'
        verbose_name = _('home appliances')
        verbose_name_plural = _('home appliances')

class HomeAppliancesModel(models.Model):
    homeAppliance = models.ForeignKey(to=HomeAppliances, on_delete=models.CASCADE, related_name='homeAppliances')
    model = models.CharField(verbose_name=_('model'), max_length=50, blank=True)
    count = models.PositiveIntegerField(verbose_name=_('count'), default=0)
    price = models.PositiveBigIntegerField(verbose_name=_('price'), default=10000)
    discount = models.CharField(verbose_name=_('discount'), blank=True, max_length=10)
    homeApplianceImage = models.ImageField(verbose_name=_('home appliance image'), upload_to='homeAppliances/')
    Description = models.TextField(verbose_name=_('description'), max_length=300, blank=True, null=True)
    createdTime = models.DateTimeField(auto_now=True)
    updatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'home_appliances_model'
        verbose_name = _('home appliance model')
        verbose_name_plural = _('home appliances model')

class Clothes(models.Model):
    edibles = 1
    home_appliances = 2
    clothes = 3
    model_types = (
        (edibles, _('edibles')),
        (home_appliances, _('home_appliances')),
        (clothes, _('clothes')))
    model_type = models.PositiveIntegerField(verbose_name=_('model type'), choices=model_types, default=clothes)
    clothe_type = models.CharField(verbose_name=_('clothe type'), max_length=30)
    is_available = models.BooleanField(verbose_name=_('is available'), default=True)
    createdTime = models.DateTimeField(auto_now=True)
    updatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clothes'
        verbose_name = _('clothe')
        verbose_name_plural = _('clothes')

class ClothesModel(models.Model):
    clothe = models.ForeignKey(to=Clothes, related_name='clothe', on_delete=models.CASCADE)
    size = models.PositiveIntegerField(verbose_name=_('size'), blank=True, null=True)
    color = models.CharField(verbose_name=_('color'), max_length=30, blank=True, null=True)
    count = models.IntegerField(verbose_name=_('count'), blank=True)
    price = models.PositiveBigIntegerField(verbose_name=_('price'), blank=True, default=100000)
    discount = models.CharField(verbose_name=_('discount'), blank=True, max_length=10)
    category_image = models.ImageField(verbose_name=_('clothe image'), upload_to='cothes/')
    Description = models.TextField(verbose_name=_('description'), max_length=500, blank=True, null=True)
    createdTime = models.DateTimeField(auto_now=True)
    uodatedTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'clothe_model'
        verbose_name = _('clothe model')
        verbose_name_plural = _('clothes model')

# class Categories(models.Model):
#     model_type =