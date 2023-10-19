from django import forms
from ckeditor.fields import RichTextFormField

class TiendaFormulario(forms.Form):
    producto = forms.CharField(max_length=20)
    descripcion= RichTextFormField()

class TiendaBusquedaFormulario(forms.Form):
    producto = forms.CharField(max_length=20, required=False)
