from django.db import models

# Create your models here.

class Servicios_Pet(models.Model):
    servicio = models.CharField(max_length=30)
    precio = models.FloatField()
    detalle = models.CharField(max_length=100)

class Dueño(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.CharField(max_length=40)
    
class Mascota(models.Model):
    nombre = models.CharField(max_length=15)
    raza = models.CharField(max_length=15)
    edad = models.IntegerField()