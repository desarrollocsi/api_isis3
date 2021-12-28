from rest_framework import serializers
##-------		MODELOS	--------------
from Apps.Admision.ficheros.models import Especialidades,Medicos,Turnos,Cie10
from Apps.Admision.citas.models import (Programacion,Citas,AntecedentesActoMedico,
	DiagnosticoActoMedico,ActoMedico,Historias)
from Apps.Admision.pacientes.models import PlanesHistoria,TipoAsegurado
##-------	SERIALIZADORES	--------------
from Apps.Admision.ficheros.serializers import (TurnosSerializer,ConsultoriosSerializer,
	EspecialidadesSerializer,MedicosSerializer,Cie10ListSerializer)


##-------------------------------------------------------------------------------------------
## ------------------------			SERIALIZANDO "AGENDA MEDICA"---------------------------##
##-------------------------------------------------------------------------------------------
class EspecialidadesProgSerializer(serializers.ModelSerializer):
	codigo 			= serializers.CharField(source='es_codigo')
	descripcion 	= serializers.CharField(source='es_descripcion')
	class Meta:
		model = Especialidades
		fields = ('codigo','descripcion')

class ProgMedTurSerializer(serializers.ModelSerializer):
	codigo 	= serializers.ReadOnlyField(source='pr_medico.me_codigo')
	nombre 	= serializers.ReadOnlyField(source='pr_medico.me_nombres')
	turno   = TurnosSerializer(source="pr_turno")
	consultorio   	= ConsultoriosSerializer(source="pr_consultorio")
	especialidad   	= EspecialidadesSerializer(source="pr_servicio")
	class Meta:
		model = Programacion
		fields = ('pr_numero','codigo','nombre','turno','consultorio','especialidad')

class AgendaMedicaSerializer(serializers.Serializer):
	orden = serializers.IntegerField(required=True)
	hora = serializers.CharField(max_length=5, required=True)
	horalleg = serializers.CharField(max_length=15, required=True)
	historia = serializers.IntegerField(required=True)
	paciente = serializers.CharField(max_length=75, required=True)
	cuenta 	= serializers.CharField(max_length=10, required=True)
	telefono = serializers.CharField(max_length=25, required=True)
	controla = serializers.CharField(max_length=3, required=True)
	fecha = serializers.CharField(max_length=10, required=True)
	observaciones = serializers.CharField(max_length=50, required=True)
	titular = serializers.CharField(max_length=50, required=True)
	idcita = serializers.IntegerField(required=True)
	atend = serializers.CharField(max_length=1, required=True)
	telefono2 = serializers.CharField(max_length=25, required=True)
	cond_serv = serializers.CharField(max_length=1, required=True)
	class Meta:
		fields = ('es_codigo','hora','horalleg','historia','paciente','cuenta','telefono',
		'controla','fecha','observaciones','titular','idcita','atend','telefono2','cond_serv')




##-------------------------------------------------------------------------------------------
## ------------------------			SERIALIZANDO "ACTO MEDICO"---------------------------##
##-------------------------------------------------------------------------------------------

class CitasSerializer(serializers.ModelSerializer):
	class Meta :
		model = Citas
		fields = ['ci_idcita','ci_cuenta','ci_numhist','ci_fechacita','ci_servicio','ci_programacion','ci_turno','ci_medico',
		'ci_consultorio','ci_orden','ci_horatencion','ci_observaciones','ci_indicatencion','ci_edad','ci_tipopac','ci_tipomov',
		'ci_actividad','ci_estado','ci_atend','ci_usersisa','ci_tarifaexamen']

class DiagnosticoAMSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiagnosticoActoMedico
		fields = ('id','idcie','tdx','actomedico_id')
		extra_kwargs = {'id': {'read_only':False,'required': False}}
	# def update(self,instance,validated_data):
	# 	pass

class AntecedentesAMSerializer(serializers.ModelSerializer):
	idan = serializers.IntegerField(source='an_id')
	valor = serializers.CharField(source='an_valor')
	class Meta:
		model = AntecedentesActoMedico
		fields = ('id','idan','valor','actomedico_id')
		extra_kwargs = {'id': {'read_only':False,'required': False}}
	# def update(self,instance,validated_data):
	# 	pass

class ActoMedicoSerializer(serializers.ModelSerializer):
	antecedentes = AntecedentesAMSerializer(many=True, required=False)
	diagnosticos = DiagnosticoAMSerializer(many=True, required=False)
	class Meta:
		model = ActoMedico
		fields = ('id','motivo','problema','parterial','fcardiaca','frespiratoria','tbucal',
		'taxiliar','peso','talla','icorporal','pcefalico','destino','examen','antecedentes','diagnosticos',
		'usuario','estado')
		extra_kwargs = {'estado': {'required': False}}

	def create(self,validated_data):
		antecedentes_data = validated_data.pop('antecedentes')	# Ubicando al objeto antecedentes
		diagnosticos_data = validated_data.pop('diagnosticos')  # Ubicando al objeto diagnostico
		actomedico = ActoMedico.objects.create(**validated_data)
		for antecedente_data in antecedentes_data:
			AntecedentesActoMedico.objects.create(actomedico=actomedico,**antecedente_data)
		for diagnostico_data in diagnosticos_data:
			DiagnosticoActoMedico.objects.create(actomedico=actomedico,**diagnostico_data)
		return actomedico

	def update(self,instance,validated_data):
		instance.motivo 		= validated_data['motivo']
		instance.problema 		= validated_data['problema']
		instance.parterial 		= validated_data['parterial']
		instance.fcardiaca 		= validated_data['fcardiaca']
		instance.frespiratoria 	= validated_data['frespiratoria']
		instance.tbucal 		= validated_data['tbucal']
		instance.peso 			= validated_data['peso']
		instance.talla 			= validated_data['talla']
		instance.icorporal 		= validated_data['icorporal']
		instance.pcefalico 		= validated_data['pcefalico']
		instance.destino 		= validated_data['destino']
		instance.examen 		= validated_data['examen']
		instance.usuario 		= validated_data['usuario']
		instance.save()
		### update Antecedentes
		antecedentes_ids = [item['id'] for item in validated_data['antecedentes']]
		for ante_actual in (instance.antecedentesactomedico).all():
			if ante_actual.id not in antecedentes_ids:#Si existe el id lo Elimina
				ante_actual.delete()
		for ante_new in validated_data['antecedentes']:
			if ante_new['id'] > 0:
				ante_am = AntecedentesActoMedico(id=ante_new['id'],an_id=ante_new['an_id'], an_valor=ante_new['an_valor'], actomedico=instance)
			else:
				ante_am = AntecedentesActoMedico(an_id=ante_new['an_id'], an_valor=ante_new['an_valor'], actomedico=instance)
			ante_am.save()
		### update Diagnosticos
		diagnosticos_ids = [item['id'] for item in validated_data['diagnosticos']]
		for diag_actual in (instance.diagnosticoactomedico).all():
			if diag_actual.id not in diagnosticos_ids:#Si existe el id lo Elimina
				diag_actual.delete()
		for diag_new in validated_data['diagnosticos']:
			if diag_new['id'] > 0:
				diag_am = DiagnosticoActoMedico(id=diag_new['id'],idcie=diag_new['idcie'], tdx=diag_new['tdx'],actomedico=instance)
			else:
				diag_am = DiagnosticoActoMedico(idcie=diag_new['idcie'], tdx=diag_new['tdx'],actomedico=instance)
			diag_am.save()
		return instance


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
	class Meta:
		model = Citas
		fields = ['id','orden','historia','hora','paciente','edad','medico','consultorio','sexo','estado','actomedico_id']

class IafasSerializer(serializers.ModelSerializer):
	# pl_desaseg = serializers.CharField(max_length=75, required=True)
	tipoaseg = serializers.CharField(max_length=8, required=False)
	ta_acredita = serializers.IntegerField(required=True)
	class Meta:
		model = PlanesHistoria
		fields = ['pl_desaseg','tipoaseg','ta_acredita']



########################################################################
###############		SERIALIZER LISTAR ACTO MEDICO 	####################
#########################################################################
class Cie10AMSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cie10
		fields = ('orden','codigo' ,'descripcion')

class AntecedentesAMListSerializer(serializers.ModelSerializer):
	idan = serializers.IntegerField(source='an_id')
	valor = serializers.CharField(source='an_valor')
	class Meta:
		model = AntecedentesActoMedico
		fields = ('id','idan','valor')

class DiagnosticoAMListSerializer(serializers.ModelSerializer):
	codigo	= serializers.ReadOnlyField(source='idcie.codigo')
	descripcion 	= serializers.ReadOnlyField(source='idcie.descripcion')
	class Meta:
		model = DiagnosticoActoMedico
		fields = ('id','tdx','idcie','codigo','descripcion')

class ActoMedicoListSerializer(serializers.ModelSerializer):
	diagnosticos = DiagnosticoAMListSerializer(source="diagnosticoactomedico",many=True)
	antecedentes = AntecedentesAMListSerializer(source="antecedentesactomedico",many=True)
	class Meta:
		model = ActoMedico
		fields = ('id','motivo','problema','parterial','fcardiaca','frespiratoria','tbucal',
		'taxiliar','peso','talla','icorporal','pcefalico','destino','examen','antecedentes','diagnosticos')





##---------------------------------------------------##
## ----------------PRUEBAS---------------------------##
##---------------------------------------------------##

# class TurnosProgSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Turnos
# 		fields = ['tu_codigo','tu_tipoturno']

# class MedicosSerializer(serializers.ModelSerializer):
# 	codigo 		= serializers.CharField(source='me_codigo')
# 	nombres 	= serializers.CharField(source='me_nombres')
# 	# turnos 		= TurnosProgSerializer(source="pr_turno")
# 	# programacion 	= serializers.ReadOnlyField(source='pr_medico')
# 	# turno   	= TurnosSerializer(source="pr_turno")
# 	class Meta:
# 		model = Medicos
# 		fields = ['codigo','nombres']
