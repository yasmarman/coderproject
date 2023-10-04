from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse 
from datetime import datetime
from inicio.models import Tienda

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


def cargar_producto(request, producto, descripcion):
    tienda = Tienda(producto=producto, descripcion=descripcion)
    tienda.save()
    return render(request, r'inicio\producto-nuevo.html', {})