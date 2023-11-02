from django import forms

class ProductoFomulario(forms.Form):
    
    producto = forms.ChoiceField()
    marca = forms.ChoiceField()
    categoria = forms.ChoiceField()

