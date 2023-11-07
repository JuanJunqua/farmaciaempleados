from django.db import models



class encargado(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField(max_length=3)
    email = models.EmailField()
    descripcion = models.CharField(max_length=10)
    empleo = models.CharField(max_length=64, default='encargado')
    
    

class subencargado(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField(max_length=3)
    email = models.EmailField()
    descripcion = models.CharField(max_length=10)
    empleo = models.CharField(max_length=64, default='subencargado')
    
    

class mostrador(models.Model):
    Nombre = models.CharField(max_length=64)
    Apellido = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField(max_length=3)
    email = models.EmailField()
    descripcion = models.CharField(max_length=10)
    empleo = models.CharField(max_length=64, default='mostrador')