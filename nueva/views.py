from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic.list import ListView
from nueva.models import Paleta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PaletaCreateView(CreateView):
    model = Paleta
    template_name = "nueva/crear-paleta.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha']
    success_url =  reverse_lazy('paletas')

class PaletaDeleteView(LoginRequiredMixin, DeleteView ):
        model = Paleta
        template_name = "nueva/eliminar-paleta.html"
        success_url =  reverse_lazy('paletas')

class PaletaDetailView(DetailView):
    model = Paleta
    template_name = "nueva/detalle-paleta.html"


class PaletaUpdateView(LoginRequiredMixin,UpdateView):
    model = Paleta
    template_name = "nueva/editar-paleta.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha']
    success_url =  reverse_lazy('paletas')

    
class PaletaListView(ListView):
    model = Paleta
    context_object_name = 'listado_paletas'
    template_name = "nueva/listar-paleta.html"

    def get_queryset(self):
         marca = self.request.GET.get('marca', '')
         if marca:
              paletas = self.model.objects.filter(marca__icontains=marca)
         else:     
              paletas = self.model.objects.all()
         return paletas        
