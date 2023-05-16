from django.contrib import admin
from .models import Products, Carrito, Lista

class ProductAdmin(admin.ModelAdmin):
    list_display =  ("description","price", "stock")
    search_fields = ("product_name", "brand_name", "price")
    list_filter = ("brand_name", "product_name")
    ordering = ("price",)

class ListaInLine(admin.TabularInline):
    model = Lista

class CaritoAdmin(admin.ModelAdmin):
    list_display = ("user", "total", "paid")
    ordering = ("create",)
    list_filter = ("paid",)
    inlines = [ListaInLine]


admin.site.register(Products, ProductAdmin)
admin.site.register(Carrito, CaritoAdmin)
admin.site.register(Lista)