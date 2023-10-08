from django.urls import path
from inicio.views import inicio, cargar_producto 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('producto-nuevo/<producto>/<descripcion>', cargar_producto, name='crear-producto')
]
