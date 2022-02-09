from rest_framework import serializers
from ..models.personales import *

class PersonalSerializer(serializers.Serializer):
       codigo = serializers.CharField()
       nombre = serializers.CharField()
       tipo   = serializers.CharField()
       class Meta:
            read_only_fields = serializers