
from django.shortcuts import render
from django.http import HttpResponse

from ServiciosPet.models import Servicios_Pet
#from MenuHum.forms import 
# Create your views here.

def ServiciosMasc (request):
    servpet = Servicios_Pet.objects.all()
    context = {'servpet':servpet}
    return render(request, 'servmasc.html', context=context)
 