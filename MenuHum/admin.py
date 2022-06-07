from django.contrib import admin
from MenuHum.models import Menu_Hum

# Register your models here.


@admin.register(Menu_Hum)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['producto', 'precio', 'detalle', 'is_active']