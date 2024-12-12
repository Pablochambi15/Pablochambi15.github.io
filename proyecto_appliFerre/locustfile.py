from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class MiUsuario(HttpUser):
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 3)
    
    def on_start(self):
        # Hacer una solicitud GET a la página de inicio de sesión para obtener el CSRF token
        self.response = self.client.get('/IniciarSesion/')
        # Parsear el HTML para obtener el CSRF token
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.csrf_token = self.soup.find('input', dict(name='csrfmiddlewaretoken'))['value']
    
    @task
    def iniciar_sesion(self):
        # Datos del formulario de inicio de sesión
        login_data = {
            'username': 'testuser',  # Usa un nombre de usuario válido
            'password': 'testpassword',  # Usa una contraseña válida
            'csrfmiddlewaretoken': self.csrf_token  # Agregar el CSRF token
        }
        
        # Realizamos la solicitud POST al endpoint de inicio de sesión
        response = self.client.post('/IniciarSesion/', data=login_data)
        
        # Verificamos si el inicio de sesión fue exitoso
        if response.status_code == 200:
            print("Inicio de sesión exitoso")
        else:
            print(f"Fallo en inicio de sesión: {response.status_code}")
    
    @task
    def productos(self):
        # Solicitud GET para obtener productos
        self.client.get('/productos/')
