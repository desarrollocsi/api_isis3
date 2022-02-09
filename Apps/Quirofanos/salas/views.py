from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.salas import *
from .serializers import *


@api_view(['GET'])
def salas_api_view(request):
    if request.method == 'GET':
        salas = SalasModel.objects.all().filter(sa_estado='1')
        salas_serializer = SalasSerializer(salas,many=True)
        return Response(salas_serializer.data)