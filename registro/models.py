from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Registro(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    username = models.CharField(max_length=30, blank=False, null=False)
    password = models.CharField(max_length=10 ,blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nombre_completo = models.CharField(max_length=40, blank=False, null=False)
    celular = models.CharField(max_length=10, blank=False, null=False)
    codigo_postal = models.CharField(max_length=10, blank=False, null=False)
    direccion = models.TextField(blank=False, null=False)
    ciudad = models.CharField(max_length=15, blank=False, null=False)
    provincia = models.CharField(max_length=15, blank=False, null=False)
    info_adicional = models.TextField(blank=False, null=False)


    def __str__(self):
        return self.nombre