from rest_framework import serializers
from .models import Clasificacion, Medidas, MotConcAnt, Reclamos, Servicio, Tipo_documento, Estado, Resultado, Etapa, MedioRecepcion, Tramas

class EstadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Estado
		fields = '__all__'

class EtapaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Etapa
		fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resultado
		fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tipo_documento
		fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Servicio
		fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clasificacion
		fields = '__all__'

class MedioRecepcionSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedioRecepcion
		fields = '__all__'

class MotConcAntSerializer(serializers.ModelSerializer):
	class Meta:
		model = MotConcAnt
		fields = '__all__'

class ReclamosSerializerList(serializers.ModelSerializer):
	desc_est = serializers.CharField(source='estado.er_desc', allow_null=True)
	desc_res = serializers.CharField(source='resultado.rr_desc', allow_null=True)
	class Meta:
		model = Reclamos
		fields = ['periodo','re_cod','fecha','nombres_p','paterno_p','materno_p','nro_documento_p','desc_est','desc_res']

class ReclamosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reclamos
		fields = '__all__'

class MedidasSerializer(serializers.ModelSerializer):
    fecha_implem = serializers.DateField(format="%Y-%m-%d")
    fecha_culm = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Medidas
        fields = '__all__'

class ReclamosSerializerData(serializers.ModelSerializer):
	fecha = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
	medidas = MedidasSerializer(source='reclamo_id', many=True)
	class Meta:
		model = Reclamos
		fields = '__all__'

class ReclamoTramaSerializer(serializers.ModelSerializer):
  fecha = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
  medidas = MedidasSerializer(source='reclamo_id', many=True)
  servicio = serializers.CharField(source='servicio.sr_codsusalud', allow_null=True)
  class Meta:
    model = Reclamos
    fields = '__all__'

class TramaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tramas
		fields = '__all__'





