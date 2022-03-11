from django.contrib import admin
from .models import Brands, Units, GroupProduct, Product, Warehouse, Provider, Systems, StatusObject, ObjectsCurrent, StatusEstimate, Estimate

admin.site.site_header = 'Администрирование Butler'

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'address')

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_display_links = ('name', 'country')
    list_filter = ('name', 'country')
    search_fields = ('name', 'country')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'art_butler', 'get_groups', 'price_in', 'brand')
    list_display_links = ('name', 'art_butler')
    list_filter = ('name', 'art_butler', 'group', 'brand')
    search_fields = ('name', 'art_butler', 'group', 'brand')

class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'client', 'contract')
    list_display_links = ('name', 'contract')
    list_filter = ('name', 'status', 'client', 'contract')
    search_fields = ('name', 'status', 'client', 'contract')

class EstimateAdmin(admin.ModelAdmin):
    list_display = ('object', 'date_doc', 'status_doc')
    list_display_links = ('object', 'date_doc', 'status_doc')
    list_filter = ('object', 'date_doc', 'status_doc')
    search_fields = ('object', 'date_doc', 'status_doc')

# Register your models here.
admin.site.register(Brands, BrandAdmin)
admin.site.register(Units)
admin.site.register(GroupProduct)
admin.site.register(Product, ProductAdmin)
admin.site.register(Warehouse)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Systems)
admin.site.register(StatusObject)
admin.site.register(ObjectsCurrent, ObjectAdmin)
admin.site.register(StatusEstimate)
admin.site.register(Estimate, EstimateAdmin)