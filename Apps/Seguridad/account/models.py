from django.db import models
from django.contrib.auth.models import AbstractUser
from Apps.Seguridad.menus.models import Rol,Menu

# Create your models here.
class User(AbstractUser):
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, related_name='id_rol', db_column='id_rol', null=True)
    # id_rol = models.CharField(max_length=100, blank=True, null=True)
    # rol = models.CharField(max_length=50)