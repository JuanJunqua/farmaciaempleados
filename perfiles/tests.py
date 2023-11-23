from django.test import TestCase
from django.urls import reverse
from perfiles.forms import UserRegisterForm
from django.contrib.auth.models import User

class RegistroViewTest(TestCase):

    def test_registro(self):
        form_data = {
            'username': 'asd1234',
            'password1': 'holahola12345',
            'password2': 'holahola12345',
        }

        response = self.client.post(reverse('registro'), data=form_data)

        
        

    def test_registro(self):
        response = self.client.get(reverse('registro'))

       
         
        
        self.assertIsInstance(response.context['form'], UserRegisterForm)  

   