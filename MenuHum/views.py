
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from MenuHum.models import Menu_Hum
from MenuHum.forms import ProductH_form
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.

#def MenuHuman (request):
#    prodhum = Menu_Hum.objects.all()
#    context = {'prodhum':prodhum}
#    return render(request, 'menuhum.html', context=context)

class List_productsH(ListView):
    model = Menu_Hum
    template_name= 'MenuHum/menuhum.html'
    queryset = Menu_Hum.objects.filter(is_active = True)

class Detail_productH(DetailView):
    model = Menu_Hum
    template_name= 'MenuHum/detail_productH.html'

class Create_productH(CreateView):
    model = Menu_Hum
    template_name = 'MenuHum/create_human.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk':self.object.pk})
    

class Delete_productH(DeleteView):
    model = Menu_Hum
    template_name = 'MenuHum/Delete_product.html'

    def get_success_url(self):
        return reverse('MenuHum')

class Update_productH(UpdateView):
    model = Menu_Hum
    template_name = 'MenuHum/update_product.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk})




""" def create_productH_view(request):
    if request.method == 'GET':
        form = ProductH_form()
        context ={'form':form}
        return render(request, 'create_human.html', context=context)
    else:
        form = ProductH_form(request.POST)
        if form.is_valid():
            new_product = Menu_Hum.objects.create(
                producto = form.cleaned_data['producto'],
                precio = form.cleaned_data['precio'],
                detalle = form.cleaned_data['detalle'],
                #imagen = form.cleaned_data(request.POST, request.FILES),
                active = form.cleaned_data['active']
            )
            context ={'new_product':new_product}
        return render(request, 'create_human.html', context=context)
        #return render (request, 'create_human.html', {'new_product':new_product}) """
def search_product_view(request):
    palabra_busqueda = request.GET['search']
    products = Menu_Hum.objects.filter(producto__icontains = (palabra_busqueda))
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':f'Disculpe no se encontro ningun producto con el nombre: {palabra_busqueda}'}
    return render(request, 'search_productH.html', context = context)
    #return render(request, 'search_productH.html')