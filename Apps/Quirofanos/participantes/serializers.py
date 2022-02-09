from rest_framework import serializers
from ..models.participantes import *


class TipoParticipantesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoParticipanteModel
        fields = '__all__'
        read_only_fields = fields

class ParticipantesSerializers(serializers.ModelSerializer):
    descripcion = serializers.StringRelatedField()

    class Meta:
        model = ParticipantesModel
        fields = ('cq_codiqx','cq_numero','cq_codpar','descripcion')
        read_only_fields = fields