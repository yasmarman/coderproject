from django import forms

class TiendaFormulario(forms.Form):
    producto = forms.CharField(max_length=20)
    descripcion= forms.CharField(max_length=80)

class TiendaBusquedaFormulario(forms.Form):
    producto = forms.CharField(max_length=20)
