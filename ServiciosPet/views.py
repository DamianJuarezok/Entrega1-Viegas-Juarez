from django.shortcuts import render
from django.http import HttpResponse

from ServiciosPet.models import Servicios_Pet, Dueño, Mascota
from ServiciosPet.forms import Dueño_form, Mascota_form
# Create your views here.

def ServiciosMasc (request):
    servpet = Servicios_Pet.objects.all()
    context = {'servpet':servpet}
    return render(request, 'servmasc.html', context=context)

def dueño(request):
    dueños = Dueño.objects.all()
    context = {"dueños":dueños}
    return render(request, "dueño.html", context=context)

def mascota(request):
    mascotas = Mascota.objects.all()
    context = {"mascotas":mascotas}
    return render(request, "mascota.html", context=context)
 
def registro_dueño(request):
    if request.method == 'GET':
        form = Dueño_form()
        context = {'form':form}
        return render(request, 'dueño.html', context=context)
    else:
        form = Dueño_form(request.POST)
        if form.is_valid():
            new_dueño = Dueño.objects.create(
                nombre = form.cleaned_data['nombre'],
                telefono = form.cleaned_data['telefono'],
                email = form.cleaned_data['email'],
            )
            context = {'new_dueño':new_dueño}
        return render(request, 'dueño.html', context=context)

def registro_mascota(request):
    if request.method == 'GET':
        form = Mascota_form()
        context = {'form':form}
        return render(request, 'mascota.html', context=context)
    else:
        form = Mascota_form(request.POST)
        if form.is_valid():
            new_mascota = Mascota.objects.create(
                nombre = form.cleaned_data['nombre'],
                raza = form.cleaned_data['raza'],
                edad = form.cleaned_data['edad'],
            )
            context = {'new_mascota':new_mascota}
        return render(request, 'mascota.html', context=context)