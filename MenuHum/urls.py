from django.urls import path
from MenuHum.views import MenuHuman, create_productH_view, search_product_view

urlpatterns =[
    path('', MenuHuman, name = 'MenuHum'),
    path('create_human/', create_productH_view, name = 'create_human'),
    path('search_product/', search_product_view, name = 'search_product_view'),
]