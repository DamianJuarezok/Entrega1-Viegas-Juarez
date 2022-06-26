from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre_apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.CharField(max_length=40)
    nombre_mascota = models.CharField(max_length=15)
    raza = models.CharField(max_length=15)
    edad = models.IntegerField()
    is_active = models.BooleanField(default=True)
    class servicio(models.IntegerChoices):
        Baño = 1
        Peluqueria = 2
        Uñas_y_orejas = 3
        Otro = 4

    Servicios = models.IntegerField(choices=servicio.choices)