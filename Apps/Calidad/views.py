from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 
from .models import *
from .serializers import *


#FUNCTION
def getIncidencia(idIncidencia):
    return F419Model.objects.filter(id=idIncidencia).first()

def parametsDynamic(paramets):
    PARAMETS_DYNAMIC = {
        'SUPERADMIN':{'fecha_registro__date':paramets['fecha']},
        'USUARIO':{'fecha_registro__date':paramets['fecha'],'estado':1}
    }   
    return PARAMETS_DYNAMIC[paramets['rol']]


@api_view(['POST'])
def incidencia_api_register(request):
    if request.method == 'POST':
        f419_serializer = F419Serializer(data=request.data)
        if f419_serializer.is_valid():
            f419_serializer.save()
            return Response({'message':'Se registro correctamente!!'},status=status.HTTP_201_CREATED)
        return Response(f419_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def incidencia_api_view(request,fecha,rol):
    if request.method == 'GET':
        filters = parametsDynamic(dict(fecha=fecha,rol=rol))
        f419_data = F419Model.objects.all().filter(**filters)
        if f419_data:
            f419_serializer = F419Serializer(f419_data,many=True)
            return Response(f419_serializer.data,status=status.HTTP_200_OK)
        return Response({'message':'No hay Incidencias para la fecha'},status=status.HTTP_200_OK)


@api_view(['GET','PUT'])
def incidencia_detail_api_view(request,pk):
    f419_data = getIncidencia(pk)
    if f419_data:
        if request.method == 'GET':
            f419_serializer = F419Serializer(f419_data)
            return Response(f419_serializer.data)
        if request.method == 'PUT':
            for data in request.data['detalles']:
                data['idincidencia']=request.data['id']
            f419_serializer = F419Serializer(f419_data,data = request.data)
            if f419_serializer.is_valid():
                f419_serializer.save()
                return Response({'message':'Se actualizo correctamente'})
            return Response(f419_serializer.errors)
    return Response({'message':'No se encontro dato'})


@api_view(['PUT'])
def incidencia_chance_status(request,pk):
    f419_data = getIncidencia(pk)
    if request.method == 'PUT':
        f419_serializer = F419StatusSerializer(f419_data,data=request.data)
        if f419_serializer.is_valid():
            f419_serializer.save()
            return Response({'status':True,'message':'Se actualizo correctamente'},status=status.HTTP_200_OK)
        return Response({'status':False,'erros':f419_serializer.errors})


'''VIEWS DE INVOLUCRADOS I/EA'''
@api_view(['GET'])
def involucrados_iea_api_view(request):
    if request.method == 'GET':
        involucrados_data = Involucrados.objects.filter(estado=True).all()
        involucrados_serializer = InvolucradosSerializer(involucrados_data,many=True)
        return Response(involucrados_serializer.data,status=status.HTTP_200_OK)


