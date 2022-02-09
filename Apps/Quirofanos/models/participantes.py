from django.db import models

class ParticipantesModel(models.Model):
    cq_codpar   = models.CharField(primary_key=True,max_length=2)
    cq_codiqx	= models.CharField(max_length=6)
    cq_numero	= models.CharField(max_length=2)
    mn_codigo	= models.CharField(max_length=3)
    cq_comimp	= models.DecimalField(max_digits=12, decimal_places=2)
    cq_compor	= models.DecimalField(max_digits=12, decimal_places=2)
    cq_estado	= models.CharField(max_length=1)
    cq_usuario	= models.CharField(max_length=15)
    cq_fecpro	= models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'participantes_cq'
        ordering = ['cq_codpar']

class TipoParticipanteModel(models.Model):    
    id = models.AutoField(primary_key=True)
    cq_despar = models.CharField(max_length=30)
    cq_estado = models.CharField(max_length=1)
    cq_usuario= models.CharField(max_length=15)
    cq_fecpro = models.DateTimeField()
    cq_codpar = models.OneToOneField(ParticipantesModel, related_name='descripcion', on_delete=models.CASCADE, db_column='cq_codpar')

    class Meta:
        managed = False
        db_table = 'tipo_participantes_cq'
    
    def __str__(self):
        return self.cq_despar