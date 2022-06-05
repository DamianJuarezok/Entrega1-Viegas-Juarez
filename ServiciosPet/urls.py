from django.urls import path
from ServiciosPet.views import ServiciosMasc, dueño, mascota, registro_dueño, registro_mascota

urlpatterns =[
    path('', ServiciosMasc, name = 'ServiciosPet'),
    path("dueño/", dueño, name = "dueño"),
    path("dueño/registro", registro_dueño, name = "registro_dueño"),
    path("mascota/", mascota, name= "mascota"),
    path("mascota/registro", registro_mascota, name = "registro_mascota"),
]