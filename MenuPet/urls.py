from django.urls import path
from MenuPet.views import MenuMasc, create_productP_view, search_product_view

urlpatterns =[
    path('', MenuMasc, name = 'MenuPet'),
    path('create_pet/', create_productP_view, name = 'create_human'),
    path('search_product/', search_product_view, name = 'search_product_view'),
]