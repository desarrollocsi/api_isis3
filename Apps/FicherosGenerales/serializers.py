from .models import *
from rest_framework import serializers

class CentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCosto
        fields = '__all__'

class MedioPagoSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='mediopagocodigo',required=True)
    descripcion = serializers.CharField(source='mediopagonombre',required=True)
    class Meta:
        model = MedioPago
        fields = '__all__'

class MedioPagoSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='mediopagocodigo',required=True)
    descripcion = serializers.CharField(source='mediopagonombre',required=True)
    class Meta:
        model = MedioPago
        fields = '__all__'

class TipoComprobanteSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='cm_tipcom',required=True)
    descripcion = serializers.CharField(source='cm_destic',required=True)
    class Meta:
        model = TipoComprobante
        fields = '__all__'