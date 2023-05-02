from django.db import models

# Create your models here.
class Config(models.Model):
    backgroundColor = models.CharField(max_length=150,verbose_name="Color de Fondo")
    forengroudColor = models.CharField(max_length=150,verbose_name='Color por encima')
    class meta:
        verbose_name = 'Config'
        verbose_name_plural = 'Configs'
        db_table = 'configs'
        ordering = ['id']
    def __str__(self):
        return self.backgroundColor