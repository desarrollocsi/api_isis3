from rest_framework import serializers
from .models import Especialidades,Consultorios,Turnos,Medicos,Cie10,Antecedentes

# Serializando los FICHEROS del Módulo "ADMISION".
class EspecialidadesSerializer(serializers.ModelSerializer):	
	codigo = serializers.CharField(source='es_codigo',required=False)
	descripcion = serializers.CharField(source='es_descripcion',required=True)
	usuario = serializers.CharField(source='es_usuario',required=False)
	class Meta:
		model = Especialidades
		fields = ['codigo','descripcion','usuario']
		extra_kwargs = {'codigo': {'required': False},}

class ConsultoriosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='co_codigo',required=False)
	descripcion = serializers.CharField(source='co_descripcion',required=True)
	usuario = serializers.CharField(source='co_user' ,required=False)
	class Meta:
		model = Consultorios
		fields = ['codigo','descripcion','co_descorta','usuario']

class TurnosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='tu_codigo',required=False)
	descripcion = serializers.CharField(source='tu_descripcion',required=True)
	usuario = serializers.CharField(source='tu_usuario',required=False)
	class Meta:
		model = Turnos
		fields = ['codigo','descripcion','tu_horaini' ,'tu_horafin' ,'tu_horas','tu_horario','tu_tipoturno' ,'usuario']
		# extra_kwargs = {'tu_usuario': {'required': False},
		# 'codigo': {'required': False}}

class MedicosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='me_codigo',required=False)
	descripcion = serializers.CharField(source='me_nombres',required=True)
	class Meta:
		model = Medicos
		# fields = ['codigo' ,'descripcion','me_colegio','me_rne','me_direccion','me_tipo_func',
		# 'me_fecnac']
		fields = ['codigo' ,'descripcion','me_colegio']
	# def save(self, **kwargs):
    #     try:
    #         super().save(**kwargs)
    #     except ModelError as e:
    #         raise serializers.ValidationError(e)

class Cie10ListSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(source='orden')
	class Meta:
		model = Cie10
		fields = ['id','codigo' ,'descripcion']

class AntecedentesListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Antecedentes
		fields = '__all__'