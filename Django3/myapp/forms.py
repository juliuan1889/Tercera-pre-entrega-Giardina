from django import forms
from .models import Categoria, Marca, Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class BuscarForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=100)
