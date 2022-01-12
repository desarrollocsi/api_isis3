from django.db import models
from django.contrib.auth.models import AbstractUser
from Apps.Seguridad.menus.models import Rol
from Apps.Admision.ficheros.models import Medicos

# Create your models here.
class User(AbstractUser):
    # id_rol = models.IntegerField(null=True)
    # id_medico = models.CharField(null=True,max_length=3)
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, related_name='rol', db_column='id_rol', blank=True, null=True)
    id_medico = models.ForeignKey(Medicos, models.DO_NOTHING, related_name='medico', db_column='id_medico', blank=True, null=True)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username