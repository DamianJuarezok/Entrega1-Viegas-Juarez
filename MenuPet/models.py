from django.db import models

# Create your models here.


class Menu_Pet(models.Model):
    producto = models.CharField(max_length=30)
    precio = models.FloatField()
    detalle = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'products', blank=True, null=True)