
from django.shortcuts import render
from django.http import HttpResponse

from MenuPet.models import Menu_Pet
#from MenuHum.forms import 
# Create your views here.

def MenuMasc (request):
    prodpet = Menu_Pet.objects.all()
    context = {'prodpet':prodpet}
    return render(request, 'menumasc.html', context=context)
