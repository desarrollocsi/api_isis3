from rest_framework import serializers
from ..models.anestesia import *

class AnestesiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anestesia
        fields = ('an_tipane','an_nombre','an_estado')
        read_only_fields = fields