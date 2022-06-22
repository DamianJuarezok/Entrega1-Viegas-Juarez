"""PetCafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PetCafe.settings import MEDIA_ROOT, MEDIA_URL
from PetCafe.views import index, about, login_view, logout_view, register_view, servicios
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('servicios/', servicios, name = 'servicios'),
    path('MenuHum/',include ('MenuHum.urls') ),
    path('MenuPet/',include ('MenuPet.urls') ),
    path('ServPet/',include ('ServiciosPet.urls') ),
    path('', index, name = 'index'),
    path('about/', about, name = 'about'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
