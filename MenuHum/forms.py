from django import forms
from MenuHum.models import Menu_Hum

#class ProductH_form (forms.Form):
#    producto = forms.CharField(max_length=30)
#    precio = forms.FloatField()
#    detalle = forms.CharField(max_length=100)
#    active = forms.BooleanField()

class ProductH_form(forms.ModelForm):
    class Meta:
        model = Menu_Hum
        fields = '__all__'   #Se puede detallar el campo que se quiere pasar