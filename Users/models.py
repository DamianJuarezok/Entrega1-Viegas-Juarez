from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField
# Create your models here.

#decorador is_staff Booleano. Designa si este usuario puede acceder al sitio de administración.

class Perfil_usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    telefono = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to="imagen_perfil", default="imagen_perfil/descarga.jpg") 
    #poner imagen por default para que no se rompa si no tiene imagen default=""

    def __str__(self):
        return str(self.usuario)

#class Perfil_superusuario(models.Model):
 #   super_usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="super_usuario")
  #  imagen = models.ImageField(upload_to="imagen_superu")


   

    