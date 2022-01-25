from django.db import models
from Apps.Seguridad.formulario.models import formularioc
# Create your models here.

class Menu(models.Model):
    nivel   = models.IntegerField()
    nombre  = models.CharField(max_length=50)
    padre   = models.ForeignKey('self', blank=True, null=True,related_name='id_padre',db_column='padre',on_delete=models.CASCADE)
    accion  = models.CharField(max_length=100, blank=True, null=True)
    icono   = models.CharField(max_length=50, blank=True, null=True)
    id_formularioc = models.ForeignKey(formularioc, models.DO_NOTHING,related_name='id_formularioc',db_column='id_formularioc', blank=True, null=True)
    estado  = models.BooleanField()
    class Meta:
        managed = True
        db_table = 'menu'
    def __str__(self):
        return self.nombre
    def getNombreMinuscula(self):
        return  self.nombre.lower()

class Rol(models.Model):
    nombre      = models.CharField(max_length=50)
    estado      = models.BooleanField()
    created_at  = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at  = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    menus       = models.ManyToManyField('Menu', related_name='rols', blank=True)
    class Meta:
        managed = True
        db_table = 'rol'
    def __str__(self):
        return self.nombre
