from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from django.http import HttpResponse 
from datetime import datetime
from inicio.models import Tienda
from inicio.forms import TiendaFormulario, TiendaBusquedaFormulario
from django.contrib.auth.decorators import login_required


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
            return redirect('listado')
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

@login_required
def editar_curso(request, id_curso):
    curso_a_editar = Tienda.objects.get(id=id_curso)
    if request.method == 'POST':
        formulario = TiendaFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso_a_editar.producto = data['producto']
            curso_a_editar.save()
            return redirect('listado')
        else:
            return render(request , 'editar-curso.html', {'formulario':formulario})

    formulario = TiendaFormulario(initial={'producto':curso_a_editar.producto})
    return render(request, r'inicio\editar-curso.html', {'formulario' : formulario})


@login_required
def eliminar_curso(request, id_curso):

    curso_a_eliminar = Tienda.objects.get(id=id_curso)
    curso_a_eliminar.delete()

    return redirect('listado')



def detalle_curso(request, id_curso):
    producto = Tienda.objects.get(id=id_curso)
    return render(request, r'inicio\detalle-curso.html', {'producto': producto})


