from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def busqueda_productos(request):

    return render(request,"busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
       # mensaje="Articulo Buscado: %r" %request.GET["prd"] #prd = pertenece al html del cuadro de texto
        producto=request.GET["prd"]
        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto) #metodo icontains es como si fuera  like en sql  (like nombre ="mesa")

        return render(request, "resultados_busqueda.html",{"articulos":articulos,"query":producto})
    else:
        mensaje="No has introducido nadita"
    return  HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER

        recipient_list=["carlosbm1982@yahoo.es"]
        send_mail(subject, message,email_from,recipient_list)

        return render(request, "gracias.html")
    return render(request, "contacto.html")