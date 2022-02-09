from django.db import models


class SalasModel(models.Model):
    sa_codsal = models.CharField(primary_key=True,max_length=2)
    sa_nombre = models.CharField(max_length=20)
    sa_cuidado = models.CharField(max_length=1)
    sa_estado = models.CharField(max_length=1)
    sa_usuario = models.CharField(max_length=15)
    sa_fecpro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "salas"
