from django.db import models


class Anestesia(models.Model):
    an_tipane = models.CharField(max_length=255,primary_key=True)
    an_nombre = models.CharField(max_length=255)
    an_estado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tipo_anestesia'
        ordering = ['an_nombre']