from rest_framework import serializers
from .models import Rols
from .serializers import serializers

# JLT:2021-01-21 -- Listado de Serializadores del Módulo Seguridad

class RolsSerializer(serializers.ModelSerializer):
    descripcion = serializers.CharField(source='nombre')
    codigo = serializers.IntegerField(source='id')
    class Meta:
        model   = Rols
        fields  = ['codigo','descripcion']