from rest_framework import serializers
from Apps.Admision.citas.models import Programacion
from Apps.Admision.ficheros.serializers \
	import EspecialidadesSerializer,TurnosSerializer,\
		MedicosSerializer,ConsultoriosSerializer


class ProgramacionesListSerializer(serializers.ModelSerializer):
	especialidad    = EspecialidadesSerializer(source="pr_servicio")
	consultorio    	= ConsultoriosSerializer(source="pr_consultorio")
	medico    		= MedicosSerializer(source="pr_medico")   
	turno    		= TurnosSerializer(source="pr_turno")    
	class Meta:
		model = Programacion
		fields = ['pr_numero' ,'medico' ,'consultorio' ,'especialidad' ,'turno',
		'pr_fecha','pr_estado','pr_cupos','pr_minutos','pr_tipo','pr_fechareg']


class ProgramacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Programacion
		fields = ['pr_numero' ,'pr_fecha' ,'pr_servicio' ,'pr_consultorio' ,'pr_medico','pr_turno',
		'pr_estado','pr_cupos','pr_minutos','pr_tipo' ,'pr_fechareg','pr_estado']
		extra_kwargs = {'pr_numero': {'required': False},}
		# fields = ['codigo','descripcion','tu_horaini' ,'tu_horafin' ,'tu_horas','tu_horario','tu_tipoturno' ,'tu_usuario']
		# extra_kwargs = {'tu_usuario': {'required': False},}