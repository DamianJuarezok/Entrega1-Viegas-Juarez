from django.urls import path
from MenuPet.views import MenuMasc

urlpatterns =[
    path('', MenuMasc, name = 'MenuPet')
]