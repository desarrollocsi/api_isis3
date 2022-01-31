from django.db import models

# Create your models here.

class F419Model(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_incidencia = models.DateField()
    historia = models.CharField(max_length=10)
    glosa = models.TextField()
    turno = models.IntegerField()
    estado = models.IntegerField(default=1)
    reporta_area = models.CharField(max_length=50)
    usuario_registro = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    usuario_actualizado = models.CharField(max_length=50,null=True, blank=True)
    fecha_actualizado = models.DateTimeField(null=True, blank=True)
    class Meta:
        managed = True
        db_table ='incidencia'
        ordering = ['id']


class F419DetailModel(models.Model):
    tipo = models.IntegerField()
    value = models.IntegerField()
    usuario_registro = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    idincidencia = models.ForeignKey(F419Model,related_name='detalles',on_delete=models.CASCADE,db_column='idincidencia',null=True, blank=True)
    class Meta:
        managed = True
        db_table = 'incidencia_d'


'''MODELOS DE INVOLUCRADOS I/EA'''

class Involucrados(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    usuario = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'iea_involucrados'
        ordering = ['id']

class InvolucradosDetail(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    usuario = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    idinvolucrados = models.ForeignKey(Involucrados,related_name='detalles',on_delete=models.CASCADE,db_column='idinvolucrados',null=True, blank=True)
    class Meta:
        managed = True
        db_table = 'iea_involucrados_d'
        ordering = ['id']