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
    def __str__(self):
        return self.key

class options(models.Model):
    idformulariod   = models.ForeignKey(formulariod,related_name='idformulariod_id',on_delete=models.CASCADE)
    key             = models.CharField(max_length=5,null=False)
    value           = models.CharField(max_length=50,null=False)
    def __str__(self):
        return self.value

class optionsradio(models.Model):
    idformulariod   = models.ForeignKey(formulariod,on_delete=models.CASCADE)
    key             = models.CharField(max_length=5,null=False)
    value           = models.CharField(max_length=50,null=False)
    name            = models.CharField(max_length=100)
    def __str__(self):
        return self.value