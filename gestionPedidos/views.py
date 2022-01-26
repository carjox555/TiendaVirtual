from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContact


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
        miFormulario=FormularioContact(request.POST)
        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data
            
            send_mail(infForm['asunto'],infForm['mensaje'],
            infForm.get('email',''),['carlosbmestra@gmail.com'],)

            return render(request,"gracias.html")


    else:
        miFormulario=FormularioContact()
    
    return render(request,"formulario_cont.html",{"forms":miFormulario})

