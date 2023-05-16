from django.shortcuts import render, redirect, get_object_or_404
from Productos.models import Products, Carrito, Lista
from django.http import Http404

def mostrarCarrito(request):
    usuario = request.user
    carrito = Carrito.objects.get(user=usuario)
    productos = Lista.objects.filter(order=carrito)
    context = {
        'productos': productos,
    }
    return render(request, 'carrito/mostrar_carrito.html', context)


def modificarCarrito(request, id):
    cantidad = request.GET.get('actualizar')
    usuario = request.user
    carrito = Carrito.objects.get(user=usuario)
    producto = Lista.objects.get(id=id, order=carrito)
    if cantidad != None:
        producto.amount = cantidad
    producto.save()
    productos = Lista.objects.filter(order=carrito)
    context = {
        'productos': productos,
    }
    return render(request, 'carrito/mostrar_carrito.html', context)

    

def eliminarProducto(request, id):
    usuario = request.user
    carrito = Carrito.objects.get(user=usuario)
    producto = get_object_or_404(Lista, id=id)
    try:
        producto.delete()
        productos = Lista.objects.filter(order=carrito)
        context = {
            'productos': productos,
        }
        return render(request, 'carrito/mostrar_carrito.html', context)
    except Lista.DoesNotExist:
        raise Http404("El producto no existe")
