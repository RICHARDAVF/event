from django.contrib import admin
from .models import ClienteUser
# Register your models here.
class AdminClinte(admin.ModelAdmin):
   
        
    list_display = ('id','ruc','usuario','password')
    list_editable = ('ruc','usuario','password')
    search_fields = ('ruc','usuario')
    list_filter = ('ruc','usuario')
    ordering = ('id',)

admin.site.register(ClienteUser,AdminClinte)

class AdminProducto(admin.ModelAdmin):
    list_display = ('id','producto','descripcion','stock','precio','descuento')
    list_editable = ('descripcion','precio','descuento')
    search_fields = ('producto','precio','descuento')
    list_filter = ('producto','stock','precio','descuento')
    ordering = ('id','stock','precio')