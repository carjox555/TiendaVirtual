from django.db import models

# Create your models here.
 
from django.db import models

# una clase por cada tabla q se necesita en la bd

class Clientes(models.Model):
    #campos  y tipo de datos 
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50,verbose_name="Tu Direccion")
    email=models.EmailField(blank=True,null=True)
    telf=models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' %(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()