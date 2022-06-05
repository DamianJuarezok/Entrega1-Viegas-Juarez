
from django.shortcuts import render
from django.http import HttpResponse

from MenuHum.models import Menu_Hum
from MenuHum.forms import ProductH_form 
# Create your views here.

def MenuHuman (request):
    prodhum = Menu_Hum.objects.all()
    context = {'prodhum':prodhum}
    return render(request, 'menuhum.html', context=context)

def create_productH_view(request):
    if request.method == 'GET':
        form = ProductH_form()
        context = {'form':form}
        return render(request, 'create_human.html', context=context)
    else:
        form = ProductH_form(request.POST)
        if form.is_valid():
            new_product = Menu_Hum.objects.create(
                producto = form.cleaned_data['producto'],
                precio = form.cleaned_data['precio'],
                detalle = form.cleaned_data['detalle'],
                active = form.cleaned_data['active'],
            )
            context ={'new_product':new_product}
        return render(request, 'create_human.html', context=context)

def search_product_view(request):
    print(request.GET)
    #product = Menu_Hum.objects.get()
    products = Menu_Hum.objects.filter(producto__contains = request.GET['search'])
    context = {'products':products}
    return render(request, 'search_productH.html', context = context)
    #return render(request, 'search_productH.html')