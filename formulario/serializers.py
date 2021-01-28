from rest_framework import serializers
from .models import formularioc,formulariod,options
from .serializers import serializers


class optionsSerializer(serializers.ModelSerializer):
    codigo = serializers.CharField(source='value')
    descripcion = serializers.CharField(source='name')
    class Meta:
        model   = options
        fields  = ['id','key','codigo','descripcion',]

class formulariodSerializer(serializers.ModelSerializer):
    options         = optionsSerializer(source='formulariod_id',many=True)
    class Meta:
        model   = formulariod
        fields  = ['value','key','label','controltype','type','order','options','tabla']

# -- ----------     SERIALIZADOR DE FORMULARIOC ->JOIN FORMULARIOD ->JOIN OPTIONS     ---------
class formularioSerializer(serializers.ModelSerializer):
    formulariod = formulariodSerializer(source='formularioc_id',many=True)
    class Meta:
        model   = formularioc
        fields  = ['id','nombre','estado','formulariod']

# -- ----------     SERIALIZADOR DE FORMULARIOC     ---------
class formulariocSerializer(serializers.ModelSerializer):
    class Meta:
        model   = formularioc
        fields  = ['id','nombre','estado']
