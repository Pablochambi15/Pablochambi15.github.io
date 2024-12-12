from django.test import TestCase
from django.urls import reverse
from .models import Producto
from decimal import Decimal
from .forms import ProductoForm

class ProductoTestCase(TestCase):
    
    def setUp(self):
         
 
        self.producto = Producto.objects.create(
            nombre='ProductoInicial',
            descripcion='Descripción inicial',
            precio=Decimal('100'),
            cantidad=100
        )
        
        
                    
    def test_crear_producto(self):
         
        producto = Producto.objects.get(nombre='ProductoInicial')
        self.assertEqual(producto.descripcion, 'Descripción inicial')
        self.assertEqual(producto.precio, Decimal('100'))
        self.assertEqual(producto.cantidad, 100)
        
      
            
    
    def test_editar_producto(self):
 
        url = reverse('productos')   
        data = {
            'action': 'editar',
            'producto_id': self.producto.id,
            'nombre': 'ProductoEditado',
            'descripcion': 'Descripción editada',
            'precio': 150,
            'cantidad': 150
            
        }
        
        response = self.client.post(url, data)
        self.producto.refresh_from_db()   
        self.assertEqual(response.status_code, 302)   
        self.assertEqual(self.producto.nombre, 'ProductoEditado')    
        self.assertEqual(self.producto.precio, 150)   
        self.assertEqual(self.producto.cantidad, 150)
        self.assertEqual(self.producto.descripcion, 'Descripción editada')
        

    def test_eliminar_producto(self):
      
        url = reverse('productos')   
        data = {
            'action': 'eliminar',
            'producto_id': self.producto.id
        }
        
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)   
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(id=self.producto.id)   
            
   

            

