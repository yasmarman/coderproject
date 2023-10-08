from django.urls import path
from inicio.views import inicio, cargar_producto , subir_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    #path('producto-nuevo/<producto>/<descripcion>', cargar_producto, name='crear-producto'),
    path('producto-nuevo/crear', cargar_producto, name='crear-producto'),
    path('crear-producto/subir', subir_producto, name='subir-producto')
]
