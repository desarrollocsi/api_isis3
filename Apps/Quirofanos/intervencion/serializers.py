from rest_framework import serializers
from ..models.intervencion import *


class IntervencionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Intervencion
        fields = ('cq_codiqx', 'cq_nomint', 'se_codigo', 'cq_tiempo')
        read_only_fields = fields