from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.mostrarCarrito, name='carrito'),
    path('<int:id>', views.modificarCarrito, name="modificar"),
    path('borrar/<int:id>', views.eliminarProducto, name="eliminar"),
]