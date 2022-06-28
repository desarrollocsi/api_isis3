from django.db import models

# Create your models here.

class CentroCosto(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    descr = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True, null=False)
    class Meta:
        managed = True
        db_table ='centrocosto'
    
class MedioPago(models.Model):
    mediopagoid = models.AutoField(primary_key=True)
    mediopagocodigo = models.CharField(max_length=3, unique=True, blank=True, null=True)
    mediopagonombre = models.CharField(max_length=30)
    class Meta:
        managed = False #isis2
        db_table ='mediodepago'

class TipoComprobante(models.Model):
    cm_tipcom = models.CharField(max_length=2,primary_key=True)
    cm_destic = models.CharField(max_length=20)
    cm_abrtic = models.CharField(max_length=20)
    class Meta:
        managed = False #isis2
        db_table ='tipo_comprobantes'