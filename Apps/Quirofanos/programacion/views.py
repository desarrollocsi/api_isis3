from django.db.models import Max
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
#
from ..models.programacion import *
from .serializers import *


def getProgramacion(numeroDeProgramacion):
    return ProgramacionModel.objects.filter(cq_numope=numeroDeProgramacion).first()

def getProgramacionParticipacion(numeroDeProgramacion):
    return ProgramacionParticipantesModel.objects.filter(cq_numope=numeroDeProgramacion).count()


@api_view(['POST'])
def programaciones_api_view(request):
    #Se obtiene el maximo numero de operacion
    data = ProgramacionModel.objects.aggregate(cq_numope=Max('cq_numope'))
    #Se genera el correlativo de numero de operacion
    numeroOperacion = str(int(data['cq_numope']) + 1).rjust(10,'0')
    if request.method == 'POST':
        request.data['cq_numope'] = numeroOperacion
        for data in request.data['participantes']:
            data['sa_codsal'] = request.data['sa_codsal']
            data['se_codigo'] = request.data['se_codigo']
        serializer = ProgramacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Se registro correctamente!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def programacion_detalle_api_view(request,pk):
    programacion_data = getProgramacion(pk)
    if programacion_data :
        if request.method == 'GET':
            programacion_serializer = ProgramacionSerializer(programacion_data)          
            return Response(programacion_serializer.data,status=status.HTTP_200_OK)

        if request.method == 'PUT':
            for data in request.data['participantes']:
                data['sa_codsal'] = request.data['sa_codsal']
                data['cq_numope'] = request.data['cq_numope']
                data['se_codigo'] = request.data['se_codigo']
            programacion_serializer = ProgramacionSerializer(programacion_data,data = request.data)
            if programacion_serializer.is_valid():
                programacion_serializer.save()
                return Response({'message':'Se actualizo correctamente!!'},status=status.HTTP_200_OK)
            return Response(programacion_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'No se encontro datos'},status=status.HTTP_400_BAD_REQUEST)