from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from ServiciosPet.models import Servicio
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.

class List_productsS(ListView):
    
    model = Servicio
    template_name= 'ServiciosPet/solserv.html'
    
    
class Detail_productS(DetailView):
    model = Servicio
    template_name= 'ServiciosPet/detail_products.html'

class Create_productS(CreateView):
    model = Servicio
    template_name = 'ServiciosPet/create_serv.html'
    fields = ['nombre_apellido', 'telefono', 'email', 'nombre_mascota', 'raza', 'edad', 'Servicios']

    def get_success_url(self):
        return reverse('detail_products', kwargs={'pk':self.object.pk})

class Delete_productS(DeleteView):
    model = Servicio
    template_name = 'ServiciosPet/delete_products.html'

    def get_success_url(self):
        return reverse('Servicios')

class Update_productS(UpdateView):
    model = Servicio
    template_name = 'ServiciosPet/update_products.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_products', kwargs = {'pk':self.object.pk})

""" def search_product_view(request):
    print(request.GET)
    products = Servicio.objects.filter(nombre_apellido__contains = request.GET['search'])
    print(2)
    context = {'products':products}
    print(3)
    return render(request, 'search_productS.html', context = context) """

def search_product_view(request):
    palabra_busqueda = request.GET['search']
    products = Servicio.objects.filter(nombre_apellido__icontains = (palabra_busqueda))
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':f'Disculpe no se encontro ningun servicio con el propietario: {palabra_busqueda}'}
    return render(request, 'search_products.html', context = context)
    