 
 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto
class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=100, required=True)
    apellidos = forms.CharField(max_length=100, required=True)
    fecha_nacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2024)), required=True)

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellidos', 'email', 'fecha_nacimiento', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password1")
        cpassword = cleaned_data.get("password2")
        if password != cpassword:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']