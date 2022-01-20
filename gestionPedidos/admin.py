from re import search
from django.contrib import admin
from gestionPedidos.models import Clientes,Articulos,Pedidos

# Register your models here.

# Aqui se guarda lo que debe salir en la pagina admin 

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion", "telf")
    search_fields=("nombre","telf")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos,ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)

