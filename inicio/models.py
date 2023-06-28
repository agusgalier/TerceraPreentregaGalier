from django.db import models

# Create your models here.

class Futbolista(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    posicion=models.CharField(max_length=20)
    
class Basquetbolista(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    posicion=models.CharField(max_length=20)
    
class Tenista(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    ranking=models.IntegerField()       
