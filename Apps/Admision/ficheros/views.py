from django.db.models import Max

from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django_filters import rest_framework as filters
# 1.- Modelos Ficheros:
from .models import Especialidades,Consultorios,Turnos,Medicos,Antecedentes
# 2.- Modelos Pacientes:
from ..pacientes.models import Paises,EstadosCiviles,TipoDocumentosPersonales,Ocupaciones

# Serializando Ficheros
from .serializers import (EspecialidadesSerializer,ConsultoriosSerializer,TurnosSerializer,MedicosSerializer,AntecedentesListSerializer,
PasisesSerializer,EstadosCivilesSerializer,TiposdeDocumentosSerializer,OcupacionesSerializer)


from rest_framework.exceptions import APIException
from django.db.models import Max
# from rest_framework import serializers

# Create your views here.
from rest_framework.permissions import IsAuthenticated

# --------------------------------------------------------------------------------------------
# ------------------------------------- VIEWS -----------------------------------------------
# --------------------------------------------------------------------------------------------

class AntecedentesList(generics.ListCreateAPIView):
    serializer_class = AntecedentesListSerializer
    def get_queryset(self):
        queryset = Antecedentes.objects.all()
        return queryset

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# VIEWS , CRUD del Módulo "ADMISION -FICHEROS".
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     ESPECIALIDADES      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""

@api_view(['GET', 'PUT', 'DELETE'])
def ESPECIALIDADES_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Especialidades.objects.get(es_codigo=pk) 
    except Especialidades.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = EspecialidadesSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        del respuestadata['fecha']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = EspecialidadesSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        try:
            objeto.delete()
            return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:            
            return Response({'status': False,'message': str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def ESPECIALIDADES_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Especialidades.objects.all().order_by('-es_codigo')
        serializer = EspecialidadesSerializer(objeto, many=True)        
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("Especialidades","es_codigo",3)
        serializer = EspecialidadesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     TURNOS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def TURNOS_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Turnos.objects.get(tu_codigo=pk) 
    except Turnos.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = TurnosSerializer(objeto)
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario'] 
        del respuestadata['fecha']
        return Response(respuestadata) 
    elif request.method == 'PUT': 
        serializer = TurnosSerializer(objeto, data = request.data)        
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        try:
            objeto.delete()
            return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False,'message': str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def TURNOS_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Turnos.objects.all().order_by('-tu_codigo')
        serializer = TurnosSerializer(objeto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("Turnos","tu_codigo",3)
        serializer = TurnosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     CONSULTORIOS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def CONSULTORIOS_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Consultorios.objects.get(co_codigo=pk) 
    except Consultorios.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = ConsultoriosSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        del respuestadata['fecha']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = ConsultoriosSerializer(objeto, data = request.data)
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        try:
            objeto.delete()
            return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False,'message': str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def CONSULTORIOS_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Consultorios.objects.all().order_by('-co_codigo')
        serializer = ConsultoriosSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("Consultorios","co_codigo",3)
        serializer = ConsultoriosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     MEDICOS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def MEDICOS_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Medicos.objects.get(me_codigo=pk) 
    except Medicos.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = MedicosSerializer(objeto) 
        return Response(respuesta.data) 
    elif request.method == 'PUT': 
        serializer = MedicosSerializer(objeto, data = request.data)
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        try:
            objeto.delete()
            return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False,'message': str(e)},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def MEDICOS_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':        
        objeto = Medicos.objects.all().order_by('-me_codigo')        
        serializer = MedicosSerializer(objeto, many=True)
        # return Response({'status': True})
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("Medicos","me_codigo",3)
        request.data['me_tipomedico'] = '001'
        serializer = MedicosSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except BaseException as be:
                print(be)
                raise APIException(detail=be.message)
                # raise serializers.ValidationError(detail.message_dict)
                # return Response({'status': False,'message': detail.message_dict}, status=status.HTTP_400_BAD_REQUEST)
            # serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# VIEWS , CRUD del Módulo "ADMISION -FICHEROS".
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     PAISES      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def PAISES_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Paises.objects.get(pa_codigo=pk) 
    except Especialidades.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = PasisesSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = PasisesSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def PAISES_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Paises.objects.all().order_by('-pa_codigo')
        serializer = PasisesSerializer(objeto, many=True)        
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("Paises","pa_codigo",3)
        serializer = PasisesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     ESTADOS CIVILES      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def ESTADOSCIVILES_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = EstadosCiviles.objects.get(ec_codigo=pk) 
    except EstadosCiviles.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = EstadosCivilesSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = EstadosCivilesSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def ESTADOSCIVILES_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = EstadosCiviles.objects.all().order_by('-ec_codigo')
        serializer = EstadosCivilesSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("EstadosCiviles","ec_codigo",3)
        serializer = EstadosCivilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■     TIPOS DE DOCUMENTOS PERSONALES      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def TIPOSDEDOCUMENTOS_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = TipoDocumentosPersonales.objects.get(td_codigo=pk) 
    except TipoDocumentosPersonales.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = TiposdeDocumentosSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = TiposdeDocumentosSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def TIPOSDEDOCUMENTOS_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = TipoDocumentosPersonales.objects.all().order_by('-td_codigo')
        serializer = TiposdeDocumentosSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("TipoDocumentosPersonales","td_codigo",3)
        serializer = TiposdeDocumentosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■             OCUPACIONES       ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def OCUPACIONES_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Ocupaciones.objects.get(op_codigo=pk) 
    except Ocupaciones.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = OcupacionesSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = OcupacionesSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def OCUPACIONES_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Ocupaciones.objects.all().order_by('-op_codigo')
        serializer = OcupacionesSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['codigo'] = f_generar_codigo("Ocupaciones","op_codigo",3)
        serializer = OcupacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




## ===========================  LISTA DE FUNCIONES DE PROCESO   =========================== ##

def f_generar_codigo(nombreDelModel,nombreDelCampo,Longitud):
    expresion = f"{nombreDelModel}.objects.aggregate({nombreDelCampo}=Max('{nombreDelCampo}'))['{nombreDelCampo}']"
    rows = eval(expresion) or 0
    return str(int(rows)+1).rjust(Longitud,'0')