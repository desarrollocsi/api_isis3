from rest_framework import serializers
from .models import Especialidades,Consultorios,Turnos,Medicos,Cie10,Antecedentes

from ..pacientes.models import Paises,EstadosCiviles,TipoDocumentosPersonales,Ocupaciones
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Serializando los FICHEROS del Módulo "ADMISION".
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class EspecialidadesSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='es_codigo',required=False)
	descripcion = serializers.CharField(source='es_descripcion',required=True)
	usuario = serializers.CharField(source='es_usuario',required=False)
	fecha = serializers.CharField(source='es_fecpro',required=False)
	class Meta:
		model = Especialidades
		fields = ['codigo','descripcion','fecha','usuario']
		extra_kwargs = {'codigo': {'required': False},}

class ConsultoriosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='co_codigo',required=False)
	descripcion = serializers.CharField(source='co_descripcion',required=True)
	usuario = serializers.CharField(source='co_user' ,required=False)
	fecha = serializers.CharField(source='co_fecpro',required=False)
	class Meta:
		model = Consultorios
		fields = ['codigo','descripcion','co_descorta','co_tipo','fecha','usuario']
	# def create(self,validated_data):
	# 	validated_data['co_codigo'] = "030"
	# 	obj = Consultorios.objects.create(**validated_data)
	# 	return obj

class TurnosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='tu_codigo',required=False)
	descripcion = serializers.CharField(source='tu_descripcion',required=True)
	usuario = serializers.CharField(source='tu_usuario',required=False)
	fecha = serializers.CharField(source='tu_fechareg',required=False)
	class Meta:
		model = Turnos
		fields = ['codigo','descripcion','tu_horaini' ,'tu_horafin' ,'tu_horas','tu_horario','tu_tipoturno','fecha' ,'usuario']
		# extra_kwargs = {'tu_usuario': {'required': False},
		# 'codigo': {'required': False}}

class MedicosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='me_codigo',required=False)
	descripcion = serializers.CharField(source='me_nombres',required=False)
	fecha = serializers.CharField(source='me_fechareg',required=False)	
	class Meta:
		model = Medicos
		# fields = ['codigo' ,'descripcion','me_colegio','me_rne','me_direccion','me_tipo_func',
		# 'me_fecnac']
		fields = ['codigo', 'me_colegio', 'me_tipomedico', 'descripcion', 'fecha', 'me_estado','me_especialidad', 
		'me_usuario', 'me_ruc', 'me_direccion', 'me_telefonofijo', 'me_telefonocelular', 'me_intervalo', 'me_correo',
		'me_tipo_func', 'me_docid','me_adicionales', 'me_extras', 'cmdco', 'me_apaterno', 'me_amaterno', 'me_pnombre',
		'me_snombre', 'me_domicilio', 'me_ubigeo', 'me_cpostal', 'me_telefonoficina', 'me_correo2', 'me_fecnac', 'me_ubigeonac',
		'me_tpodocumento', 'me_nrodocumento', 'me_foto', 'me_rne', 'me_regdroga', 'me_anexo', 'me_colegioval', 'me_rutafoto',
		'me_sexo']
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


#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Serializando Módulo "PACIENTES":
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class PasisesSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='pa_codigo',required=False)
	descripcion = serializers.CharField(source='pa_descripcion',required=True)
	nacionalidad = serializers.CharField(source='pa_nacionalidad',required=True)
	usuario = serializers.CharField(source='pa_usuario',required=False)
	class Meta:
		model = Paises
		fields = ['codigo' ,'descripcion','nacionalidad','usuario']

class EstadosCivilesSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='ec_codigo',required=False)
	descripcion = serializers.CharField(source='ec_descripcion',required=True)
	abreviado = serializers.CharField(source='ec_abv',required=True)
	usuario = serializers.CharField(source='ec_usuario',required=False)
	class Meta:
		model = EstadosCiviles
		fields = ['codigo' ,'descripcion','abreviado','usuario']

class TiposdeDocumentosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='td_codigo',required=False)
	descripcion = serializers.CharField(source='td_descripcion',required=True)
	abreviado = serializers.CharField(source='td_abv',required=True)
	usuario = serializers.CharField(source='td_usuario',required=False)
	abreviado2 = serializers.CharField(source='td_abv2',required=False)
	class Meta:
		model = TipoDocumentosPersonales
		fields = ['codigo' ,'descripcion','abreviado','usuario','abreviado2']

class OcupacionesSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='op_codigo',required=False)
	descripcion = serializers.CharField(source='op_descripcion',required=True)
	abreviado = serializers.CharField(source='op_abv',required=True)
	usuario = serializers.CharField(source='op_usuario',required=False)
	class Meta:
		model = Ocupaciones
		fields = ['codigo' ,'descripcion','abreviado','usuario']