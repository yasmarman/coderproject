from django.urls import path
from inicio.views import inicio, cargar_producto 

urlpatterns = [
    path('', inicio),
    path('producto-nuevo/<producto>/<descripcion>', cargar_producto)
]
