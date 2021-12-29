from django.db import models
# Importando Modelos .
from Apps.Admision.ficheros.models import Especialidades,Turnos,Medicos,Consultorios,Cie10,Antecedentes
from Apps.Admision.pacientes.models import Historias

from datetime import datetime
# from dateutil.relativedelta import relativedelta

# Create your models here.

## ----------------------------------------------------------------------------------------------------------------------
## Modelo que no se migra
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    class Meta:
        managed = True
        db_table = 'citas_reporter'
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
## ----------------------------------------------------------------------------------------------------------------------

class Programacion(models.Model):
    pr_numero = models.CharField(primary_key=True, max_length=8)
    pr_medico = models.ForeignKey(Medicos, models.DO_NOTHING, related_name='pr_medico', db_column='pr_medico', blank=True, null=True)
    pr_consultorio = models.ForeignKey(Consultorios, models.DO_NOTHING, related_name='pr_consultorio', db_column='pr_consultorio', blank=True, null=True)
    pr_servicio = models.ForeignKey(Especialidades,models.DO_NOTHING, related_name='pr_servicio', db_column='pr_servicio', blank=True, null=True)
    pr_turno = models.ForeignKey(Turnos, models.DO_NOTHING, related_name='pr_turno', db_column='pr_turno', blank=True, null=True)
    pr_fecha = models.CharField(max_length=10, blank=True, null=True)
    pr_estado = models.CharField(max_length=1, blank=True, null=True)
    pr_cupos = models.IntegerField(blank=True, null=True)
    pr_minutos = models.IntegerField(blank=True, null=True)
    pr_tipo = models.CharField(max_length=1, blank=True, null=True)
    pr_fechareg = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    pr_usuario = models.CharField(max_length=15, blank=True, null=True)
    pr_observ = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'programacion'


class ActoMedico(models.Model):
    id = models.BigAutoField(primary_key=True)
    motivo = models.TextField(blank=True, null=True)
    problema = models.TextField(blank=True, null=True)
    parterial = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fcardiaca = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frespiratoria = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tbucal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    taxiliar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    talla = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    icorporal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pcefalico = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    examen = models.TextField(blank=True, null=True)
    planes = models.TextField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    cod_final = models.CharField(max_length=6, blank=True, null=True)
    des_fina = models.CharField(max_length=50, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True,default=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)
    usuario = models.CharField(max_length=15, blank=True, null=True)
    # default=datetime.now()

    class Meta:
        managed = True
        db_table = 'acto_medico'
    def __str__(self):
        return "%s %s" % (self.id, self.motivo)


class AntecedentesActoMedico(models.Model):
    id = models.BigAutoField(primary_key=True)
    # idcita = models.IntegerField()
    # idcita = models.ForeignKey(Citas,models.DO_NOTHING, related_name='ante_idcita', db_column='idcita', blank=True, null=True)
    actomedico = models.ForeignKey(ActoMedico, models.DO_NOTHING, related_name='antecedentesactomedico', db_column='actomedico_id', blank=False, null=False, default=0)
    an_id = models.IntegerField()
    an_valor = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = True
        db_table = 'antecedentes_acto_medico'
    def __str__(self):
        return "%s" % (self.id)


class DiagnosticoActoMedico(models.Model):
    id = models.BigAutoField(primary_key=True)
    # idcita = models.IntegerField()
    # idcita = models.ForeignKey(Citas,models.DO_NOTHING, related_name='diag_idcita', db_column='idcita',blank=True, null=True)
    actomedico = models.ForeignKey(ActoMedico, models.DO_NOTHING, related_name='diagnosticoactomedico', db_column='actomedico_id', blank=False, null=False)
    # idcie = models.IntegerField()
    idcie = models.ForeignKey(Cie10,models.DO_NOTHING, related_name='diagcie10', db_column='idcie', blank=True, null=True)
    tdx = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        managed = True
        db_table = 'diagnostico_acto_medico'
    def __str__(self):
        return "%s" % (self.id)


class Citas(models.Model):
    ci_idcita           = models.AutoField(primary_key=True)
    ci_cuenta           = models.CharField(max_length=10,blank=True)
    ci_numhist          = models.ForeignKey(Historias,models.DO_NOTHING, related_name='ci_numhist', db_column='ci_numhist', blank=True, null=True) # models.CharField(max_length=10)
    # ci_numhist        = models.ForeignKey('Historias', on_delete=models.CASCADE, null=True)
    # hc_numhist        = models.ForeignKey("Historias",verbose_name="Historia",on_delete=models.CASCADE, null=True, db_column='ci_numhist')
    # ci_numhist        = models.ForeignKey(Historias, related_name='citas', on_delete=models.CASCADE, null=True)
    ci_fechacita        = models.DateTimeField(blank=True, null=True)
    ci_servicio         = models.ForeignKey(Especialidades,models.DO_NOTHING,related_name='ci_servicio', db_column='ci_servicio', blank=True, null=True)
    ci_programacion     = models.ForeignKey(Programacion,models.DO_NOTHING,related_name='ci_programacion', db_column='ci_programacion', blank=True, null=True)
    # ci_turno          = models.CharField(max_length=3, blank=True, null=True)
    ci_turno            = models.ForeignKey(Turnos,models.DO_NOTHING,related_name='ci_turno', db_column='ci_turno', blank=True, null=True)
    # ci_medico         = models.CharField(max_length=3, blank=True, null=True)
    ci_medico           = models.ForeignKey(Medicos,models.DO_NOTHING,related_name='ci_medico', db_column='ci_medico', blank=True, null=True)
    #ci_consultorio     = models.CharField(max_length=3, blank=True, null=True)
    ci_consultorio      = models.ForeignKey(Consultorios,models.DO_NOTHING,related_name='ci_consultorio', db_column='ci_consultorio', blank=True, null=True)
    ci_orden            = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ci_horatencion      = models.CharField(max_length=5, blank=True, null=True)
    ci_observaciones    = models.CharField(max_length=50, blank=True, null=True)
    ci_indicatencion    = models.CharField(max_length=5, blank=True, null=True)
    ci_edad             = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    ci_tipopac          = models.CharField(max_length=5, blank=True, null=True)
    ci_tipomov          = models.CharField(max_length=3, blank=True, null=True)
    ci_actividad        = models.CharField(max_length=3, blank=True, null=True)
    ci_estado           = models.CharField(max_length=1, blank=True, null=True)
    ci_facturada        = models.IntegerField(blank=True, null=True)
    ci_pagada           = models.IntegerField(blank=True, null=True)
    ci_atend            = models.TextField(blank=True, null=True)  # This field type is a guess.
    ci_terminal         = models.CharField(max_length=15, blank=True, null=True)
    ci_userterm         = models.CharField(max_length=15, blank=True, null=True)
    ci_usersisa         = models.CharField(max_length=15, blank=True, null=True)
    ci_fecpro           = models.DateTimeField(blank=True, null=True)
    ci_indatos          = models.IntegerField(blank=True, null=True)
    ci_dxcie            = models.CharField(max_length=6, blank=True, null=True)
    ci_dxcie2           = models.CharField(max_length=6, blank=True, null=True)
    ci_tarifaexamen     = models.CharField(max_length=2, blank=True, null=True)
    ci_tarifa           = models.CharField(max_length=3, blank=True, null=True)
    ci_contratante      = models.CharField(max_length=6, blank=True, null=True)
    ci_numfac           = models.CharField(max_length=12, blank=True, null=True)
    ci_coaseg           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ci_cofarm           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ci_coserv           = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ci_nroid            = models.CharField(max_length=12, blank=True, null=True)
    ci_paciente         = models.CharField(max_length=98, blank=True, null=True)
    ci_codsx            = models.CharField(max_length=1, blank=True, null=True)
    ci_coded            = models.IntegerField(blank=True, null=True)
    ci_tel1             = models.CharField(max_length=15, blank=True, null=True)
    ci_tel2             = models.CharField(max_length=15, blank=True, null=True)
    actomedico_id       = models.ForeignKey(ActoMedico, models.DO_NOTHING, related_name='citasactomedico', db_column='actomedico_id', blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'citas'
    def __str__(self):
        return f'{self.ci_cuenta} {self.ci_numhist}'




class PlantillaAgenda(models.Model):
    # co_codigo = models.AutoField(auto_created=True,primary_key=True, serialize=False, verbose_name='co_codigo')
    orden = models.BigAutoField(primary_key=True)
    hora = models.CharField(max_length=5, null=True,blank=True)
    horalleg = models.CharField(max_length=15, null=True,blank=True)
    historia = models.CharField(max_length=10, null=True,blank=True)
    paciente = models.CharField(max_length=75, null=True,blank=True)
    cuenta 	= models.CharField(max_length=10, null=True,blank=True)
    telefono = models.CharField(max_length=25, null=True,blank=True)
    controla = models.CharField(max_length=3, null=True,blank=True)
    fecha = models.CharField(max_length=10, null=True,blank=True)
    observaciones = models.CharField(max_length=50, null=True,blank=True)
    titular = models.CharField(max_length=50, null=True,blank=True)
    idcita = models.IntegerField(null=True)
    atend = models.CharField(max_length=1, null=True,blank=True)
    telefono2 = models.CharField(max_length=25, null=True,blank=True)
    cond_serv = models.CharField(max_length=1, null=True,blank=True)

    class Meta:
        managed = True
        db_table = 'plantilla_agenda'
    def __str__(self):
        return "%s %s" % (self.orden, self.hora)


# class CitasReporter(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)

#     class Meta:
#         managed = False
#         db_table = 'citas_reporter'