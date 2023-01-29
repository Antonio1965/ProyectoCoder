from django.db import models

# Create your models here.

class Estudiante(models.Model):
  
  nombre = models.CharField(max_length=40)
  apellido = models.CharField(max_length=40)
  cumple = models.DateField()
  
class Curso(models.Model):
  
  nombre = models.CharField(max_length=40)
  camada = models.IntegerField()
  
class Profersor(models.Model):
  nombre = models.CharField(max_length=40)
  apellido = models.CharField(max_length=40)
  email = models.EmailField()
    
class Entregable(models.Model):
  nombre = models.CharField(max_length=30)
  fechaDeEntrega = models.DateField()
  entregado = models.BooleanField()    
  
class Familiar(models.Model):
  parentesco = models.CharField(max_length=40)
  nombre = models.CharField(max_length=40)
  edad =  models.IntegerField()
  fecha = models.DateField()