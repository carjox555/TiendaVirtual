from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):

    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
       # mensaje="Articulo Buscado: %r" %request.GET["prd"] #prd = pertenece al html del cuadro de texto
        producto=request.GET["prd"]
        articulos=Articulos.objects.filter(nombre__icontains=producto) #metodo icontains es como si fuera  like en sql  (like nombre ="mesa")

        return render(request, "resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="No has introducido nadita"
    return  HttpResponse(mensaje)