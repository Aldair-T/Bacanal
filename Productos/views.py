from django.shortcuts import render, redirect
from .models import Products, Carrito, Lista
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages


def mostrarProductos(request):
    last_search = request.session.get('last_search')
    """if last_search:
        productos = Products.objects.filter(description__icontains = last_search)
    else:"""
    productos = Products.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos/productos.html', context)


def busquedaProducto(request):
    busqueda = request.GET.get('search')
    request.session['last_search'] = busqueda
    productos = Products.objects.filter(description__icontains = busqueda).order_by("-stock")
    context = {
        'productos': productos,
    }
    return render(request, 'productos/busqueda_productos.html', context)


def agregaraCarrito(request, id):
    producto_agg = Products.objects.get(id=id)
    cantidad = request.GET.get('añadir')
    usuario = request.user
    carrito = Carrito.objects.get(user=usuario)
    if Lista.objects.filter(order=carrito, product=producto_agg):
        Lista.objects.filter(order=carrito, product=producto_agg).update(amount=cantidad)
    else:
    #productos = Lista.objects.filter(order=carrito_id) esta es la forma de ingresar a la lista de productos
        Lista.objects.create(product=producto_agg, order=carrito, amount=cantidad, price=producto_agg.price)
    messages.success(request, "El producto se agrego al carrito")
    return redirect('catalogo')

def productos(request):
    fernets = Products.objects.filter(product_name__icontains="Fernet").order_by("-stock","-price")[:6]
    vodkas = Products.objects.filter(product_name__icontains="Vodka").order_by("-stock","-price")[:6]
    cervezas = Products.objects.filter(product_name="fernet").order_by("-price")[:6]
    context = {
        'fernets': fernets,
        'vodkas': vodkas
    }
    return render(request, 'productos/producto.html', context)
 