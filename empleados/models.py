from django.db import models
from django.contrib.auth.models import User


class encargado(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    email = models.EmailField()
    descripcion = models.CharField(max_length=100)
    empleo = models.CharField(max_length=64, default='encargado')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    

class subencargado(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    email = models.EmailField()
    descripcion = models.CharField(max_length=100)
    empleo = models.CharField(max_length=64, default='subencargado')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    

class mostrador(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    email = models.EmailField()
    descripcion = models.CharField(max_length=100)
    empleo = models.CharField(max_length=64, default='mostrador')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)






class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    