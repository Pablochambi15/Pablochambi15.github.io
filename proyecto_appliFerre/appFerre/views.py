from django.shortcuts import redirect, render, get_object_or_404
from .forms import UsuarioForm, ProductoForm
from django.contrib.auth import authenticate, login
from .models import Producto
from django.http import JsonResponse
from django.db import IntegrityError

# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Página de soporte
def soporte(request):
    return render(request, 'soporte.html')

# Inicio de sesión
def IniciarSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('sistema')   
        else:
            error = "Usuario o contraseña incorrectos"
            return render(request, 'IniciarSesion.html', {'error': error})

    return render(request, 'IniciarSesion.html')

# Registro de usuarios
def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password1'])   
            usuario.save()
            print("Formulario válido. Usuario creado.")   
            return redirect('IniciarSesion')   
        else:
            print("Formulario inválido. Errores:", form.errors)  
    else:
        form = UsuarioForm()

    return render(request, 'registro.html', {'form': form})

# Página del sistema principal
def sistema(request):
    return render(request, 'sistema.html')

# Página de almacén detallado
def almacen_detallado(request):
    return render(request, 'almacen_detallado.html')

# Página de proveedores
def proveedores(request):
    return render(request, 'proveedores.html')

# Gestión de productos
def productos(request):
    productos = Producto.objects.all()
    form = ProductoForm()

    if request.method == 'POST':
        action = request.POST.get('action')
        producto_id = request.POST.get('producto_id')

        if action == 'crear':
            form = ProductoForm(request.POST)
            if form.is_valid():
                print("Datos válidos:", form.cleaned_data)  # Depuración
                form.save()
                return redirect('productos')
            else:
                print("Errores en el formulario:", form.errors)  # Depuración
        elif action == 'editar' and producto_id:
            producto = get_object_or_404(Producto, pk=producto_id)
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                print("Datos válidos:", form.cleaned_data)  # Depuración
                form.save()
                return redirect('productos')
            else:
                print("Errores en el formulario:", form.errors)  # Depuración
        elif action == 'eliminar' and producto_id:
            producto = get_object_or_404(Producto, pk=producto_id)
            producto.delete()
            return redirect('productos')

    return render(request, 'productos.html', {
        'productos': productos,
        'form': form,
    })
