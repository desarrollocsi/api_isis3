from django.db import models


class Intervencion(models.Model):
    cq_codiqx = models.CharField(max_length=255,primary_key=True)
    cq_nomint = models.CharField(max_length=255)
    se_codigo = models.CharField(max_length=255)
    cq_tiempo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'intervenciones_cq'
        ordering = ['cq_nomint']