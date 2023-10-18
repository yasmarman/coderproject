from django.urls import path
from inicio.views import inicio, cargar_producto , subir_producto, listado_producto, editar_curso, eliminar_curso, detalle_curso

urlpatterns = [
    path('', inicio, name='inicio'),
    #path('producto-nuevo/<producto>/<descripcion>', cargar_producto, name='crear-producto'),
    path('producto-nuevo/crear', cargar_producto, name='crear-producto'),
    path('crear-producto/subir', subir_producto, name='subir-producto'),
    path('productos', listado_producto, name='listado'),
    path('editar-curso/<int:id_curso>/editar/', editar_curso, name='editar-curso'),
    path('editar-curso/<int:id_curso>/eliminar/', eliminar_curso, name='eliminar-curso'),
    path('editar-curso/<int:id_curso>/', detalle_curso, name='detalle-curso'),
]
