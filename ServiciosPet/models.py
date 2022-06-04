from django.db import models

# Create your models here.

class Servicios_Pet(models.Model):
    servicio = models.CharField(max_length=30)
    precio = models.FloatField()
    detalle = models.CharField(max_length=100)