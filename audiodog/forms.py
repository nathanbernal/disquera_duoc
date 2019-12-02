from django import forms

from .models import Usuario

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nombre', 'rut', 'email', 'telefonos', 'ciudad', 'dispositivo')
