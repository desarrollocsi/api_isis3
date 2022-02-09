from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#
from ..models.participantes import *
from .serializers import *


@api_view(['GET'])
def participantes_api_view(request, pk):
    if request.method == 'GET':
        participantes = ParticipantesModel.objects.all().filter(cq_codiqx = pk)
        participantes_serializers = ParticipantesSerializers(participantes,many=True)  
        return Response(participantes_serializers.data)


