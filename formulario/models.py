from django.db import models

# Create your models here.
class formularioc(models.Model):
    nombre      = models.CharField(max_length=100,null=False)
    estado      = models.BooleanField()
    fecharegistro = models.DateTimeField(auto_now=False)
    fechamodificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class formulariod(models.Model):
    formularioc     = models.ForeignKey(formularioc,related_name='formularioc_id',on_delete=models.CASCADE)
    value           = models.CharField(max_length=100,null=True,blank=True)
    key             = models.CharField(max_length=50,null=False)
    label           = models.CharField(max_length=80,null=False)
    controltype     = models.CharField(max_length=50,null=False)
    type            = models.CharField(max_length=50,null=False)
    order           = models.IntegerField(null=True)
    tabla            = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.key


class options(models.Model):
    formulariod   = models.ForeignKey(formulariod,related_name='formulariod_id',on_delete=models.CASCADE)
    key             = models.CharField(max_length=5,null=True,blank=True)
    value           = models.CharField(max_length=50,null=False)
    name            = models.CharField(max_length=100)
    def __str__(self):
        return self.name