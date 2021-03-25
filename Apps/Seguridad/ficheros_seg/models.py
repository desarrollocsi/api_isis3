from django.db import models

# Create your models here.

# class Menus(models.Model):
#     nivel = models.IntegerField()
#     nombre = models.CharField(max_length=50)
#     padre = models.IntegerField()
#     accion = models.CharField(max_length=100)
#     icono = models.CharField(max_length=50)
#     estado = models.BooleanField()
#     iduser = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'menus'

# class Rols(models.Model):
#     nombre = models.CharField(max_length=50)
#     superadmin = models.BooleanField()
#     estado = models.BooleanField()
#     iduser = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'rols'
#     def __str__(self):
#         return self.nombre

# class MenusRols(models.Model):
#     id_rol = models.OneToOneField('Rols', models.DO_NOTHING, db_column='id_rol', primary_key=True)
#     id_menu = models.ForeignKey(Menus, models.DO_NOTHING, db_column='id_menu')
#     iduser = models.IntegerField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'menus_rols'
#         unique_together = (('id_rol', 'id_menu'),)