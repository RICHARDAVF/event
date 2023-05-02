from django.db import models
from django.contrib.auth.hashers import make_password,check_password
# Create your models here.
class ClienteUser(models.Model):
    ruc = models.CharField(max_length=20,verbose_name='RUC')
    usuario = models.CharField(max_length=55,verbose_name='Usuario')
    password = models.CharField(max_length=254,verbose_name='Contraseña')
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = "Clientes"
        db_table = 'clientes'
        ordering = ['id']
    
    def __str__(self):
        return self.usuario
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
class Productos(models.Model):
    producto = models.CharField(max_length=100,verbose_name='Producto')
    descripcion = models.CharField(max_length=555,verbose_name="Descripcion de Producto")
    stok = models.PositiveIntegerField(verbose_name="Stock de Producto")
    precio = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Precio Producto")
    descuento = models.DecimalField(max_digits=9,decimal_places=2,verbose_name="Descuento")
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['id']