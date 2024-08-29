from django.contrib import admin
from inventory_app.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'price', 'inventory_count', 'category', 'sales_count', 'popularity_score')
    readonly_fields = ['popularity_score', 'sales_count',]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'sale_date')

admin.site.register( Product, ProductAdmin)
admin.site.register( Category, CategoryAdmin)
admin.site.register( Sale, SaleAdmin)