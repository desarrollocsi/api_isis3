from django.db import models

class ProgramacionModel(models.Model):
    cq_numope = models.CharField(primary_key=True,max_length=10)
    sa_codsal = models.CharField(max_length=2,null=True, blank=True)
    cq_fecha  = models.DateTimeField(null=True, blank=True)
    cq_hoinpr = models.DateTimeField(null=True, blank=True)
    cq_hofipr = models.DateTimeField(null=True, blank=True)
    cq_indrep = models.CharField(max_length=1,null=True, blank=True)
    cq_hoinre = models.DateTimeField(null=True, blank=True)
    cq_hofire = models.DateTimeField(null=True, blank=True)
    cq_hoinej = models.DateTimeField(null=True, blank=True)
    cq_hofiej = models.DateTimeField(null=True, blank=True)
    se_codigo = models.CharField(max_length=3,null=True, blank=True)
    cq_codiqx = models.CharField(max_length=6,null=True, blank=True)
    an_tipane = models.CharField(max_length=2,null=True, blank=True)
    cq_cuenta = models.CharField(max_length=10,null=True, blank=True)
    cq_numhis = models.CharField(max_length=10,null=True, blank=True)
    cq_tipcon = models.CharField(max_length=5,null=True, blank=True)
    cq_cama   = models.CharField(max_length=6,null=True, blank=True)
    cq_estado = models.CharField(max_length=1,null=True, blank=True)
    cq_indfac = models.CharField(max_length=1, default='0',null=True, blank=True)
    cq_paciente = models.CharField(max_length=99,null=True, blank=True)
    cq_pedido = models.CharField(max_length=199,null=True, blank=True)
    cq_usuario = models.CharField(max_length=15,null=True, blank=True)
    cq_fecpro = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    cq_edad = models.CharField(max_length=2,null=True, blank=True)
    cq_glosa_repro = models.CharField(max_length=200,null=True, blank=True)
    cq_num_petito = models.CharField(max_length=10,null=True, blank=True)
    cq_es_emer = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_orden_cq = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_usua_mod_est = models.CharField(max_length=15,null=True, blank=True)
    cq_fecha_mod_est = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    cq_orden_rqx = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_numsema = models.CharField(max_length=10,null=True, blank=True)
    cq_areapre = models.CharField(default='SD',max_length=2,null=True, blank=True)
    cq_codiqx2 = models.CharField(max_length=6,null=True, blank=True)
    cq_estd_suspendida = models.CharField(max_length=1,null=True, blank=True)
    cq_es_adelan = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_enfer = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_antibio = models.CharField(max_length=50,default='0',null=True, blank=True)
    cq_kg = models.CharField(max_length=2,null=True, blank=True)
    cq_btb = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_reing = models.CharField(max_length=1,default='0',null=True, blank=True)
    cq_estancia = models.CharField(max_length=2,null=True, blank=True)
    cq_codiqx3 = models.CharField(max_length=6,null=True, blank=True)
    cq_motivo_suspen = models.CharField(max_length=200,null=True, blank=True)
    cq_hg = models.CharField(max_length=5,null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'programacion_cq'
        

class ProgramacionParticipantesModel(models.Model):
    id = models.AutoField(primary_key=True)
    cq_codpar = models.CharField(max_length=2,null=True, blank=True)
    sa_codsal = models.CharField(max_length=2, null=True, blank=True)
    cq_numero = models.CharField(max_length=2,null=True, blank=True)
    se_codigo = models.CharField(max_length=3, null=True, blank=True)
    cq_codiqx = models.CharField(max_length=6, null=True, blank=True)
    ar_codare = models.CharField(max_length=2, null=True, blank=True)
    pl_codper = models.CharField(max_length=8, null=True, blank=True)
    cq_estado = models.CharField(default='1',max_length=1, null=True, blank=True)
    cq_observ = models.CharField(max_length=100,null=True, blank=True)    
    cq_numope = models.ForeignKey(ProgramacionModel, related_name='participantes', on_delete=models.CASCADE, db_column='cq_numope',null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'programacion_cq_d'


class ProgramacionEquiposMedicosModel(models.Model):
    id = models.AutoField(primary_key=True)
    de_codequi = models.CharField(max_length=3,null=True, blank=True)
    de_uso = models.CharField(max_length=1, default='1', null=True, blank=True)
    de_numope = models.ForeignKey(ProgramacionModel, related_name='equiposMedicos', on_delete=models.CASCADE, db_column='de_numope',null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'det_prog_equi_cq'
