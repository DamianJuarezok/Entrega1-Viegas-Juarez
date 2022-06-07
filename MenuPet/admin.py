from django.contrib import admin
from MenuPet.models import Menu_Pet

# Register your models here.

@admin.register(Menu_Pet)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['producto', 'precio', 'detalle', 'is_active']