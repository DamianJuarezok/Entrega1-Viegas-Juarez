from django.urls import path
from MenuHum.views import  search_product_view, DeleteView, List_productsH, Detail_productH, Create_productH, Delete_productH, Update_productH, Edit_productsH

urlpatterns =[
    #path('', MenuHuman, name = 'MenuHum'),
    path('', List_productsH.as_view(), name = 'MenuHum'),
    path('create_human/', Create_productH.as_view(), name = 'create_products'),
    path('editar_human/', Edit_productsH.as_view(), name = 'edit_products'),
    #path('create_human/', create_productH_view, name = 'create_human'),
    path('detail-product/<int:pk>/', Detail_productH.as_view(), name = 'detail_product'),
    path('delete-product/<int:pk>/', Delete_productH.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_productH.as_view(), name = 'update_product'),
    path('search_product/', search_product_view, name = 'search_product_view'),
]