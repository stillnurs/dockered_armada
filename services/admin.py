from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ServiceListCategory)
class ServiceListAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ServicePanel)
class ServicePanelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

    # def in_category(self, obj):
    #     return "\n".join([a.title for a in obj.category.all()])


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Staff)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ContactClient)
class ContactClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['body', 'title']


@admin.register(Equipment)
class EquipmentCarousel(admin.ModelAdmin):
    list_display = ['carousel_text']
