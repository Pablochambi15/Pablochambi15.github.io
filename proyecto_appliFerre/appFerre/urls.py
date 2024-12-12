from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name='inicio'),
    path('soporte/', views.soporte, name='soporte'),
    path('IniciarSesion/', views.IniciarSesion, name='IniciarSesion'),
    path('registro/', views.registro, name="registro"),
    path('sistema/', views.sistema, name='sistema'),
    path('productos/', views.productos, name='productos'),
 
 
    path('almacen_detallado/', views.almacen_detallado, name='almacen_detallado'),
    path('proveedores/', views.proveedores, name='proveedores'),
     
     

]
