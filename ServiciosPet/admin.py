from django.contrib import admin
from ServiciosPet.models import Servicios_Pet, Dueño, Mascota

# Register your models here.

admin.site.register (Servicios_Pet)
admin.site.register (Dueño)
admin.site.register (Mascota)