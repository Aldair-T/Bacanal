from django.shortcuts import render, redirect
from .forms import RegistroForm, PerfilForm
from .models import Registro
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from Productos.models import Carrito

def index(request):
    return render(request, 'registro/index.html', {})

def registrarse(request):
    
    if request.method == 'GET':
        form = RegistroForm()
        context = {
            'form': form
        }

        return render(request, 'registro/registrarse.html', context)
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        usuario_ingresado = request.POST['username']
        email_ingresado = request.POST['email']
        usuarios_existentes = Registro.objects.filter(username=usuario_ingresado)
        email_existentes = Registro.objects.filter(email=email_ingresado)
        
        context = {
            'form' : form,
        } 

        if usuarios_existentes.count() >= 1:
            messages.success(request, 'Usuario ya existente')
            return render(request, 'registro/registrarse.html', context)

        elif email_existentes.count() >= 1:
            messages.success(request, 'Este correo ya esta en uso')
            return render(request, 'registro/registrarse.html', context)

        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'El usuario se creo con exito')
                return redirect('registro')

@login_required
@csrf_protect
def verPerfil(request):
    usuario = request.user
    form = PerfilForm()
    context = {
        'form': form,
        'user': usuario
    }
    carrito = Carrito.objects.filter(user=usuario)
    if not carrito:
        Carrito.objects.create(total=0, user=usuario)
    return render(request, 'registro/perfil.html', context)


def crearPerfil(request):
    
    if request.method == 'GET':
        form = PerfilForm()
        context = {
            'form' : form
        }
        return render(request,'registro/crear.html',context)
    
    if request.method == 'POST':
        usuario = request.user
        form = PerfilForm(request.POST)
        #form.user = request.user # esto tiene que ir dentro del html
        if form.is_valid():
            form.Meta.model.user = usuario
            form.save()
            return redirect('perfil')
        else:
            return HttpResponse(form)