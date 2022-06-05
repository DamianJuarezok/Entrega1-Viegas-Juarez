from django import forms
from MenuPet.models import Menu_Pet

#class ProductH_form (forms.Form):
#    producto = forms.CharField(max_length=30)
#    precio = forms.FloatField()
#    detalle = forms.CharField(max_length=100)
#    active = forms.BooleanField()

class ProductP_form(forms.ModelForm):
    class Meta:
        model = Menu_Pet
        fields = '__all__'   #Se puede detallar el campo que se quiere pasar