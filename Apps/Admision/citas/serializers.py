from rest_framework import serializers
from Apps.Admision.citas.models \
	import Programacion,Citas,Historias,AntecedentesActoMedico,DiagnosticoActoMedico,ActoMedico
from Apps.Admision.ficheros.serializers \
	import EspecialidadesSerializer,TurnosSerializer,\
		MedicosSerializer,ConsultoriosSerializer,Cie10ListSerializer,AntecedentesListSerializer


class HistoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Historias
		fields = '__all__'

class HistoriaSerializerList(serializers.ModelSerializer):
	class Meta:
		model = Historias
		fields = ['hc_numhis','hc_apepat','hc_apemat','hc_nombre','hc_fecnac']

class ProgramacionesListSerializer(serializers.ModelSerializer):
	especialidad    = EspecialidadesSerializer(source="pr_servicio")
	consultorio    	= ConsultoriosSerializer(source="pr_consultorio")
	medico    		= MedicosSerializer(source="pr_medico")
	turno    		= TurnosSerializer(source="pr_turno")
	class Meta:
		model = Programacion
		fields = ['pr_numero' ,'medico' ,'consultorio' ,'especialidad' ,'turno',
		'pr_fecha','pr_estado','pr_cupos','pr_minutos','pr_tipo']


class ProgramacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Programacion
		fields = ['pr_numero' ,'pr_fecha' ,'pr_servicio' ,'pr_consultorio' ,'pr_medico','pr_turno',
		'pr_estado','pr_cupos','pr_minutos','pr_tipo' ,'pr_fechareg']
		extra_kwargs = {'pr_numero': {'required': False},}
		# fields = ['codigo','descripcion','tu_horaini' ,'tu_horafin' ,'tu_horas','tu_horario','tu_tipoturno' ,'tu_usuario']
		# extra_kwargs = {'tu_usuario': {'required': False},}

class CitasListSerializer(serializers.ModelSerializer):
	id 			= serializers.IntegerField(source='ci_idcita')
	orden 		= serializers.IntegerField(source='ci_orden')
	historia 	= serializers.ReadOnlyField(source='ci_numhist.hc_numhis')
	hora 		= serializers.CharField(source='ci_horatencion')
	paciente	= serializers.ReadOnlyField(source='ci_numhist.getNombreCompleto')
	edad 		= serializers.ReadOnlyField(source='ci_numhist.getEdad')
	medico 		= serializers.ReadOnlyField(source='ci_medico.me_nombres')
	consultorio = serializers.ReadOnlyField(source="ci_consultorio.co_descripcion")
	sexo 		= serializers.ReadOnlyField(source='ci_numhist.hc_sexo')
	estado 		= serializers.CharField(source='ci_estado')
	# medico    		= MedicosSerializer(source="ci_medico")
	# fullname	= serializers.SerializerMethodField()
	# ci_medico 	= serializers.SerializerMethodField()
	class Meta:
		model = Citas
		fields = ['id','orden','historia','hora','paciente','edad','medico','consultorio','sexo','estado',]
		# def get_ci_medico(selft, obj):
		# 	medico = obj.ci_medico
		# 	if medico:
		# 		return ci_medico.me_nombres
		# 	return None
class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields= ['ci_idcita','ci_numhist','ci_programacion','ci_fechacita','ci_horatencion',
                'ci_estado','ci_servicio','ci_medico','ci_consultorio']

class DiagnosticoAMSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiagnosticoActoMedico
		fields = ('idcita','idcie','tdx')

class AntecedentesAMSerializer(serializers.ModelSerializer):
	idan = serializers.CharField(source='an_id')
	valor = serializers.CharField(source='an_valor')
	class Meta:
		model = AntecedentesActoMedico
		fields = ('idcita','idan','valor')

class ActoMedicoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActoMedico
		fields = ('idcita','motivo','problema','parterial','fcardiaca','frespiratoria','tbucal',
		'taxiliar','peso','talla','icorporal','pcefalico','destino','examen')



