from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class Clientes_Admin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")

class Articulos_Admin(admin.ModelAdmin):
    list_filter=("seccion",)

admin.site.register(Clientes, Clientes_Admin)
admin.site.register(Articulos, Articulos_Admin)
admin.site.register(Pedidos)