from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse 
from datetime import datetime
from inicio.models import Tienda
from inicio.forms import TiendaFormulario, TiendaBusquedaFormulario


def inicio(request):

    datos = {'fecha' :datetime.now }
    #template = loader.get_template(r'inicio\inicio.html')
    #template_renderizad = template.render(datos)
    #return HttpResponse(template_renderizad)


    return render(request, r'inicio\inicio.html', datos)


    #archivo = open(r'inicio\templates\inicio\inicio.html', 'r')
    #template = Template(archivo.read())
    #archivo.close()
    #contexto = Context()
    #template_renderizado = template.render(contexto)
    #return HttpResponse(template_renderizado)


#def cargar_producto(request, producto, descripcion):
   # tienda = Tienda(producto=producto, descripcion=descripcion)
   # tienda.save()
    #return render(request, r'inicio\producto-nuevo.html', {})


def cargar_producto(request):
   
    return render(request, r'inicio\producto-nuevo.html', {})

def subir_producto(request):
    
    if request.method == 'POST':
        formulario = TiendaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            tienda = Tienda(producto = data.get('producto'), descripcion = data['descripcion'])
            tienda.save()
        else:
            return render(request, r'inicio\crear-producto.html', {'formulario': formulario})
    formulario = TiendaFormulario()
    return render(request, r'inicio\crear-producto.html', {'formulario': formulario})



def listado_producto(request):

    formulario = TiendaBusquedaFormulario(request.GET)
    if formulario.is_valid():
        producto_buscado = formulario.cleaned_data.get('producto')
        listado = Tienda.objects.filter(producto__icontains = producto_buscado)
    else:
        listado = Tienda.objects.all()
    
    formulario = TiendaBusquedaFormulario()
    return render(request, r'inicio\productos.html', {'formulario': formulario, 'listado':listado})
