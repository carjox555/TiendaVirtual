from django.db import models

# Create your models here.
 
from django.db import models

# una clase por cada tabla q se necesita en la bd

class Clientes(models.Model):
    #campos  y tipo de datos 
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telf=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El precio es %s la seccion es %s y el precio es %s' %(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()