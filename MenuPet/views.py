
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from MenuPet.models import Menu_Pet
#from MenuPet.forms import ProductP_form

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.

class Edit_productsM(ListView):
    model = Menu_Pet
    template_name= 'MenuPet/editarmenu.html'
    
    def get_success_url(self):
        return reverse('detail-product', kwargs={'pk':self.object.pk})
    


class List_productsM(ListView):
    model = Menu_Pet
    template_name= 'MenuPet/menumasc.html'
    queryset = Menu_Pet.objects.filter(is_active = True)

class Detail_productM(DetailView):
    model = Menu_Pet
    template_name= 'MenuPet/detail_productm.html'

class Create_productM(CreateView):
    model = Menu_Pet
    template_name = 'MenuPet/create_pet.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_productm', kwargs={'pk':self.object.pk})

class Delete_productM(DeleteView):
    model = Menu_Pet
    template_name = 'MenuPet/Delete_productm.html'

    def get_success_url(self):
        return reverse('MenuPet')

class Update_productM(UpdateView):
    model = Menu_Pet
    template_name = 'MenuPet/update_productm.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_productm', kwargs = {'pk':self.object.pk})

""" def search_product_view(request):
    print(request.GET)
    #product = Menu_Hum.objects.get()
    products = Menu_Pet.objects.filter(producto__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_productP.html', context = context)
    #return render(request, 'search_productH.html') """

def search_product_view(request):
    palabra_busqueda = request.GET['search']
    products = Menu_Pet.objects.filter(producto__icontains = (palabra_busqueda))
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':f'Disculpe no se encontro ningun producto con el nombre: {palabra_busqueda}'}
    return render(request, 'search_productP.html', context = context)