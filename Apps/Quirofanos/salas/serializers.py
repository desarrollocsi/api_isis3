from rest_framework import serializers
from ..models.salas import *


class SalasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalasModel
        fields = ('sa_codsal','sa_nombre','sa_cuidado')
        read_only_fields = fields