from rest_framework import serializers
from .models import formularioc,formulariod,options,optionsradio
from .serializers import serializers


class optionsSerializer(serializers.ModelSerializer):
    class Meta:
        model   = options
        fields  = ['id','key','value']

class optionsradioSerializer(serializers.ModelSerializer):
    class Meta:
        model   = optionsradio
        fields  = ['id','key','value','name']

class formulariodSerializer(serializers.ModelSerializer):
    optionsradio    = optionsSerializer(source='idformulariod_id',many=True)
    options         = optionsSerializer(source='idformulariod_id',many=True)
    class Meta:
        model   = formulariod
        fields  = ['value','key','label','controltype','type','order','options','optionsradio']

class formularioSerializer(serializers.ModelSerializer):
    formulariod = formulariodSerializer(source='formularioc_id',many=True)
    class Meta:
        model   = formularioc
        fields  = ['id','nombre','estado','formulariod']
