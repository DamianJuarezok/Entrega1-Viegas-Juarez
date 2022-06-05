
from django.shortcuts import render
from django.http import HttpResponse

from MenuPet.models import Menu_Pet
from MenuPet.forms import ProductP_form
# Create your views here.

def MenuMasc (request):
    prodpet = Menu_Pet.objects.all()
    context = {'prodpet':prodpet}
    return render(request, 'menumasc.html', context=context)

def create_productP_view(request):
    if request.method == 'GET':
        form = ProductP_form()
        context = {'form':form}
        return render(request, 'create_pet.html', context=context)
    else:
        form = ProductP_form(request.POST)
        if form.is_valid():
            new_product = Menu_Pet.objects.create(
                producto = form.cleaned_data['producto'],
                precio = form.cleaned_data['precio'],
                detalle = form.cleaned_data['detalle'],
                active = form.cleaned_data['active'],
            )
            context ={'new_product':new_product}
        return render(request, 'create_pet.html', context=context)

def search_product_view(request):
    print(request.GET)
    #product = Menu_Hum.objects.get()
    products = Menu_Pet.objects.filter(producto__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_productP.html', context = context)
    #return render(request, 'search_productH.html')