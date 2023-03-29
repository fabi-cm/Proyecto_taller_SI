from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Emprendedor, Usuario

class RegistrarUsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label="Contrasenia", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma contrasenia", widget=forms.PasswordInput)

    class Meta:
        model = Emprendedor
        fields = [
            # 'nombre_completo',
            # 'NIT',
            # 'correo',
            # 'numero_telefono',
            # 'numero_cuenta_bancaria',
            # 'banco',
            # 'img_perfil',
            'usuario',
            'nombre_representante',
            'direccion',
            'rubro',
            'descripcion',
            'password1',
            'password2',
        ]
