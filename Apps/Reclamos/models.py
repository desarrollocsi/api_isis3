from django.db import models
# Create your models here.

class Etapa(models.Model):
    etr_cod = models.IntegerField(primary_key=True)
    etr_desc = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = True

class Tipo_documento(models.Model):
    td_cod = models.IntegerField(primary_key=True)
    td_desc = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = True

class Derecho(models.Model):
    ds_cod = models.AutoField(primary_key=True)
    ds_desc = models.CharField(max_length=40, blank=True, null=True)
    class Meta:
        managed = True

class Clasificacion(models.Model):
    cr_cod = models.IntegerField(primary_key=True)
    cr_derecho = models.ForeignKey(Derecho, models.DO_NOTHING, blank=True, null=True)
    cr_def_corta = models.CharField(max_length=150, blank=True, null=True)
    cr_causa_espec = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        managed = True

class MedioRecepcion(models.Model):
    mr_cod = models.IntegerField(primary_key=True)
    mr_desc = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = True


class Estado(models.Model):
    er_cod = models.IntegerField(primary_key=True)
    er_desc = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        managed = True

class Resultado(models.Model):
    rr_cod = models.IntegerField(primary_key=True)
    rr_desc = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        managed = True

class Servicio(models.Model):
    sr_cod = models.CharField(primary_key=True, max_length=2)
    sr_desc = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        managed = True

class MotConcAnt(models.Model):
    mc_cod = models.IntegerField(primary_key=True)
    mc_desc = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        managed = True

class Reclamos(models.Model):
    re_cod = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=6,blank=True, null=True)
    cod_fisico = models.IntegerField(blank=True, null=True)
    medio = models.IntegerField(blank=True, null=True)
    tipo_documento = models.ForeignKey(Tipo_documento, models.DO_NOTHING, related_name='tipo_documento', blank=True, null=True)
    nro_documento = models.CharField(max_length=15, blank=True, null=True)
    nombres = models.CharField(max_length=150, blank=True, null=True)
    paterno = models.CharField(max_length=150, blank=True, null=True)
    materno = models.CharField(max_length=150, blank=True, null=True)
    tipo_documento_p = models.ForeignKey(Tipo_documento, models.DO_NOTHING, related_name='tipo_documento_p', blank=True, null=True)
    nro_documento_p = models.CharField(max_length=15, blank=True, null=True)
    nombres_p = models.CharField(max_length=150, blank=True, null=True)
    paterno_p = models.CharField(max_length=150, blank=True, null=True)
    materno_p = models.CharField(max_length=150, blank=True, null=True)
    result_email = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    domicilio = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    medio_recepcion = models.ForeignKey(MedioRecepcion, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    detalle = models.CharField(max_length=1500, blank=True, null=True)
    servicio = models.ForeignKey(Servicio, models.DO_NOTHING, blank=True, null=True)
    compete = models.IntegerField(blank=True, null=True)
    clasificacion1 = models.ForeignKey(Clasificacion, models.DO_NOTHING, related_name='clasificacion1', blank=True, null=True)
    clasificacion2 = models.ForeignKey(Clasificacion, models.DO_NOTHING, related_name='clasificacion2', blank=True, null=True)
    clasificacion3 = models.ForeignKey(Clasificacion, models.DO_NOTHING, related_name='clasificacion3', blank=True, null=True)
    estado = models.ForeignKey(Estado, models.DO_NOTHING, blank=True, null=True)
    codigo_original = models.CharField(max_length=15, blank=True, null=True)
    etapa = models.ForeignKey(Etapa, models.DO_NOTHING, blank=True, null=True)
    derivado_tipo = models.IntegerField(blank=True, null=True)
    derivado_codigo = models.CharField(max_length=8, blank=True, null=True)
    resultado = models.ForeignKey(Resultado, models.DO_NOTHING, blank=True, null=True)
    mot_concl_antic = models.ForeignKey(MotConcAnt, models.DO_NOTHING, blank=True, null=True)
    fecha_result = models.DateField(blank=True, null=True)
    comunic_result = models.IntegerField(blank=True, null=True)
    fecha_notif_result = models.DateField(blank=True, null=True)
    creador = models.CharField(max_length=20, blank=True, null=True)
    creacion = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modificador = models.CharField(max_length=20, blank=True, null=True)
    modificacion = models.DateTimeField(blank=True, null=True, auto_now=True)
    class Meta:
        managed = True

class NaturalezaMedida(models.Model):
    nm_cod = models.IntegerField(primary_key=True)
    nm_desc = models.CharField(max_length=60, blank=True, null=True)
    class Meta:
        managed = True

class ProcesoMedida(models.Model):
    pm_cod = models.IntegerField(primary_key=True)
    pm_desc = models.CharField(max_length=60, blank=True, null=True)
    class Meta:
        managed = True

class Medidas(models.Model):
    re_cod = models.ForeignKey(Reclamos, models.CASCADE, related_name='reclamo_id')
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    naturaleza = models.ForeignKey(NaturalezaMedida, models.SET_NULL, blank=True, null=True)
    proceso = models.ForeignKey(ProcesoMedida, models.SET_NULL, blank=True, null=True)
    fecha_implem = models.DateField(blank=True, null=True)
    fecha_culm = models.DateField(blank=True, null=True)
    class Meta:
        managed = True

class Tramas(models.Model):
    tr_cod = models.AutoField(primary_key=True)
    periodo = models.CharField(max_length=6, blank=True, null=True)
    trama = models.TextField(blank=True, null=True)
    creador = models.CharField(max_length=20, blank=True, null=True)
    creacion = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    modificador = models.CharField(max_length=20, blank=True, null=True)
    modificacion = models.DateTimeField(blank=True, null=True, auto_now=True)
    class Meta:
        managed = True


