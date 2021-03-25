from rest_framework import serializers
from .models import Menu,Rol

class Menuserializer(serializers.ModelSerializer):
    tabla = serializers.ReadOnlyField(source='id_formularioc.id')
    nombres 		= serializers.ReadOnlyField(source='getNombreMinuscula')
    # rol = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all(), many=True)
    class Meta:
        ordering = ['nivel','nombre']
        model   = Menu
        fields  = ('id','nivel','nombres','padre','accion','tabla','icono','estado')
# JLT:2021-01-21 -- Listado de Serializadores del Módulo Seguridad

class RolsSerializer(serializers.ModelSerializer):
    descripcion = serializers.CharField(source='nombre')
    codigo      = serializers.IntegerField(source='id')
    menu        = Menuserializer(many=True,source="menus")
    class Meta:
        ordering = ['codigo']
        model   = Rol
        fields  = ('codigo','descripcion','menu')
        extra_kwargs = {'menus': {'required': False}}