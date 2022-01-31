from rest_framework import serializers
from .models import *


class F419DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = F419DetailModel  
        exclude = ['id','fecha_registro']

class F419Serializer(serializers.ModelSerializer):
    detalles = F419DetailSerializer(many=True)
    class Meta:
        model = F419Model
        fields = '__all__'

    #create
    def create(self, validated_data):
        detalles = validated_data.pop('detalles')
        '''Cabecera de la Incidencias'''
        f419 = F419Model.objects.create(**validated_data)
        '''Detalle de la Incidencias'''
        for detalles in detalles:
            F419DetailModel.objects.create(idincidencia=f419, **detalles)
        return f419

    #actualizar
    def update(self, instance,validated_data):
        detalles = validated_data.pop('detalles')
        print(detalles)
        detalles_queryset = (instance.detalles).all()

        instance.fecha_incidencia=validated_data.get('fecha_incidencia',instance.fecha_incidencia)
        instance.historia=validated_data.get('historia',instance.historia)
        instance.glosa=validated_data.get('glosa',instance.glosa)
        instance.turno=validated_data.get('turno',instance.turno)
        instance.estado=validated_data.get('estado',instance.estado)
        instance.reporta_area=validated_data.get('reporta_area',instance.reporta_area)
        instance.usuario_registro=validated_data.get('usuario_registro',instance.usuario_registro)
        instance.fecha_registro=validated_data.get('fecha_registro',instance.fecha_registro)
        instance.usuario_actualizado=validated_data.get('usuario_actualizado',instance.usuario_actualizado)
        instance.fecha_actualizado=validated_data.get('fecha_actualizado',instance.fecha_actualizado)
        instance.save()

        detalles_queryset.delete()
        for detalles in detalles:
            F419DetailModel.objects.create(**detalles)
        return instance


class F419StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = F419Model
        fields = "__all__"
    
    #actualizar
    def update(self, instance,validated_data):
        instance.estado = validated_data.get('estado',instance.estado)
        instance.save()
        return instance


'''SERIALIZADOR PARA LOS MODELOS DE INVOLUCRADOS I/EA'''

class InvolucradosDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvolucradosDetail
        fields = '__all__'


class InvolucradosSerializer(serializers.ModelSerializer):
    detalles = InvolucradosDetailSerializer(many=True,read_only=True)

    @staticmethod
    def setup_eager_loading(cls, queryset):
        queryset = queryset.prefetch_related('detalles')
        return queryset

    class Meta:
        model = Involucrados
        fields = '__all__'
