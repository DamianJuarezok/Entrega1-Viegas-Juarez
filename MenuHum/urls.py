from django.urls import path
from MenuHum.views import MenuHuman

urlpatterns =[
    path('', MenuHuman, name = 'MenuHum'),
]