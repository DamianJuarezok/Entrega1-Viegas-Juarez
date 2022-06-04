from django.urls import path
from ServiciosPet.views import ServiciosMasc

urlpatterns =[
    path('', ServiciosMasc, name = 'ServiciosPet')
]