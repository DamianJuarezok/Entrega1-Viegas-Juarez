from django.urls import path
from ServiciosPet.views import search_product_view, DeleteView, List_productsS, Detail_productS, Create_productS, Delete_productS, Update_productS

urlpatterns =[
    #path('', MenuHuman, name = 'MenuHum'),
    path('list_serv/', List_productsS.as_view(), name = 'Servicios'),
    path('', Create_productS.as_view(), name = 'create_products'),
    #path('create_human/', create_productH_view, name = 'create_human'),
    path('detail-product/<int:pk>/', Detail_productS.as_view(), name = 'detail_products'),
    path('delete-product/<int:pk>/', Delete_productS.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_productS.as_view(), name = 'update_products'),
    path('search_product/', search_product_view, name = 'search_product_view'),
]