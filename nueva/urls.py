from django.urls import path
from nueva import views


urlpatterns = [
    path('paletas/',views.PaletaListView.as_view() , name='paletas'),
    path('paletas/crear/',views.PaletaCreateView.as_view() , name='crear_paletas'),
    path('paletas/<int:pk>',views.PaletaDetailView.as_view() , name='detalle_paletas'),
    path('paletas/<int:pk>/editar/',views.PaletaUpdateView.as_view() , name='editar_paletas'),
    path('paletas/<int:pk>/eliminar/', views.PaletaDeleteView.as_view(), name='eliminar_paletas'),
]
