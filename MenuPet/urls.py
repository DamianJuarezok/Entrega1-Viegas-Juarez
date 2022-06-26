from django.urls import path
from MenuPet.views import  search_product_view, DeleteView, List_productsM, Detail_productM, Create_productM, Delete_productM, Update_productM, Edit_productsM

#urlpatterns =[
#    path('', MenuMasc, name = 'MenuPet'),
#    path('create_pet/', create_productP_view, name = 'create_human'),
#    path('search_product/', search_product_view, name = 'search_product_view'),
#]

urlpatterns =[
    #path('', MenuHuman, name = 'MenuHum'),
    path('', List_productsM.as_view(), name = 'MenuPet'),
    path('editar_pet/', Edit_productsM.as_view(), name = 'edit_products'),
    path('create_pet/', Create_productM.as_view(), name = 'create_products'),
    #path('create_human/', create_productH_view, name = 'create_human'),
    path('detail-product/<int:pk>/', Detail_productM.as_view(), name = 'detail_productm'),
    path('delete-product/<int:pk>/', Delete_productM.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_productM.as_view(), name = 'update_product'),
    path('search_product/', search_product_view, name = 'search_product_view'),
]