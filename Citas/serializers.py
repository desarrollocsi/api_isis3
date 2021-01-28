from rest_framework import serializers
from .models import Especialidades,Medicos,Programacion,Consultorios,Turnos

class EspecialidadesSerializer(serializers.ModelSerializer):	
	codigo = serializers.CharField(source='es_codigo')
	descripcion = serializers.CharField(source='es_descripcion')
	class Meta:
		model = Especialidades
		fields = ['codigo','descripcion','es_usuario']
		extra_kwargs = {'es_usuario': {'required': False},}

class ConsultoriosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='co_codigo')
	descripcion = serializers.CharField(source='co_descripcion')
	class Meta:
		model = Consultorios
		fields = ['codigo','descripcion','co_descorta','co_user']
		extra_kwargs = {'co_user': {'required': False},}

class TurnosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='tu_codigo')
	descripcion = serializers.CharField(source='tu_descripcion')
	class Meta:
		model = Turnos
		fields = ['codigo','descripcion','tu_horaini' ,'tu_horafin' ,'tu_horas','tu_horario','tu_tipoturno' ,'tu_usuario']
		extra_kwargs = {'tu_usuario': {'required': False},}
		
class MedicosSerializer(serializers.ModelSerializer):
	codigo = serializers.CharField(source='me_codigo')
	descripcion = serializers.CharField(source='me_nombres')
	class Meta:
		model = Medicos
		fields = ['codigo' ,'descripcion','me_colegio']

class ProgramacionesSerializer(serializers.ModelSerializer):
	especialidad    = EspecialidadesSerializer(source="pr_servicio")
	consultorio    	= ConsultoriosSerializer(source="pr_consultorio")
	medico    		= MedicosSerializer(source="pr_medico")   
	turno    		= TurnosSerializer(source="pr_turno")    
	class Meta:
		model = Programacion
		fields = ('pr_numero' ,'medico' ,'consultorio' ,'especialidad' ,'turno',
		'pr_fecha','pr_estado','pr_cupos','pr_minutos','pr_tipo')