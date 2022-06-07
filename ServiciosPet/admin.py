from django.contrib import admin
from ServiciosPet.models import Servicio

# Register your models here.

@admin.register(Servicio)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['nombre_apellido', 'telefono', 'email', 'nombre_mascota', 'raza','edad','is_active']