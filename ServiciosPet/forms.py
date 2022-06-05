from django import forms
from ServiciosPet.models import Dueño, Mascota

class Dueño_form(forms.Form):
    nombre = forms.CharField(max_length=40)
    telefono = forms.FloatField()
    email = forms.CharField(max_length=40)

class Mascota_form(forms.Form):
    nombre = forms.CharField(max_length=15)
    raza = forms.CharField(max_length=15)
    edad = forms.IntegerField()