from django.contrib import admin

from .models import Edibles, Clothes, HomeAppliances, EdiblesModel ,ClothesModel, HomeAppliancesModel

class ClothesModelAdmin(admin.StackedInline):
    model = ClothesModel
    list_display = ['size', 'color', 'count', 'price', 'discount', 'category_image', 'Description']
    # list_filter = ['count']
    search_fields = ['clothe']
    extra = 0

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_type', 'clothe_type', 'is_available']
    # list_filter = ['price']
    inlines = [ClothesModelAdmin]

class HomeAppliancesAdmin(admin.StackedInline):
    model = HomeAppliancesModel
    list_display = ['model', 'count', 'price', 'descount', 'homeAppliancesImage', 'Description']
    # list_filter = ['count']
    extra = 0

@admin.register(HomeAppliances)
class HomeAppliancesAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_type', 'home_appliance_type', 'is_available']
    # list_filter = ['price']
    inlines = [HomeAppliancesAdmin]

class EdiblesAdmin(admin.StackedInline):
    model = EdiblesModel
    list_display = ['mark', 'taste', 'price', 'discount', 'edibleImage', 'Description']
    # list_filter = ['mark']
    extra = 0

@admin.register(Edibles)
class EdibleAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_type', 'edible_type', 'is_available']
    # list_filter = ['price']
    inlines = [EdiblesAdmin]

# Register your models here.
