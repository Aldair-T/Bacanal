from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='registro'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('perfil/', views.verPerfil, name='perfil'),
    path('crear/', views.crearPerfil, name="crearPerfil")
]
