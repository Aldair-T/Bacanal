from django import forms
from .models import Registro, Perfil

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        exclude = ['date']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = "__all__"