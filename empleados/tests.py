from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import encargado, mostrador, subencargado

class EncargadosTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_encargados(self):
        
        client = Client()
       
        client.login(username='test_user', password='test_password')

        
        form_data = {
            'Nombre': 'test',
            'Apellido': 'testing',
            'telefono': '123',
            'edad': 65,
            'email': 'test@gmail.com',
            'descripcion': 'mas test',
            'empleo': 'Encargado',
            'creador': self.user.id,  
        }

        
        response = client.post(reverse('encargados'), data=form_data)          
        self.assertRedirects(response, reverse('base'))                
        nuevo_encargado = encargado.objects.first()
        self.assertEqual(nuevo_encargado.creador, self.user)

class MostradorTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_encargados(self):
        
        client = Client()
       
        client.login(username='test_user', password='test_password')

        
        form_data = {
            'Nombre': 'test',
            'Apellido': 'testing',
            'telefono': '123',
            'edad': 65,
            'email': 'test@gmail.com',
            'descripcion': 'mas test',
            'empleo': 'Encargado',
            'creador': self.user.id,  
        }

        
        response = client.post(reverse('mostradores'), data=form_data)          
        self.assertRedirects(response, reverse('base'))                
        nuevo_mostrador = mostrador.objects.first()
        self.assertEqual(nuevo_mostrador.creador, self.user)


class SubencargadosTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_encargados(self):
        
        client = Client()
       
        client.login(username='test_user', password='test_password')

        
        form_data = {
            'Nombre': 'test',
            'Apellido': 'testing',
            'telefono': '123',
            'edad': 65,
            'email': 'test@gmail.com',
            'descripcion': 'mas test',
            'empleo': 'Encargado',
            'creador': self.user.id,  
        }

        
        response = client.post(reverse('subencargados'), data=form_data)          
        self.assertRedirects(response, reverse('base'))                
        nuevo_subencargado = subencargado.objects.first()
        self.assertEqual(nuevo_subencargado.creador, self.user)
           
