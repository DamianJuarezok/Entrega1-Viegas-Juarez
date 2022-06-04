
from django.shortcuts import render
from django.http import HttpResponse

from MenuHum.models import Menu_Hum
#from MenuHum.forms import 
# Create your views here.

def MenuHuman (request):
    prodhum = Menu_Hum.objects.all()
    context = {'prodhum':prodhum}
    return render(request, 'menuhum.html', context=context)
