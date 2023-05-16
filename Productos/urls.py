from django.urls import path
from . import views
urlpatterns = [
    path('', views.productos, name='catalogo'),
    path('<int:id>', views.agregaraCarrito, name='añadir'),
    path('busqueda/', views.busquedaProducto, name='busqueda'),
]
