from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from django_filters import rest_framework as filters
from .models import Especialidades,Consultorios,Turnos,Medicos
from .serializers import EspecialidadesSerializer,ConsultoriosSerializer,TurnosSerializer,MedicosSerializer

from rest_framework.exceptions import APIException
# from rest_framework import serializers

# Create your views here.

# -------------------------------   CRUD REST ---------------------------------------
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
        return Response(respuestadata) 
    elif request.method == 'PUT':        
        serializer = EspecialidadesSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)

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
        del request.data['codigo']
        serializer = EspecialidadesSerializer(data=request.data)
        # return Response({'status': True,'message': 'Registros grabados correctamente.',
        # "data":request.data})
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
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
        return Response(respuestadata) 
    elif request.method == 'PUT': 
        serializer = TurnosSerializer(objeto, data = request.data)        
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)

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
        del request.data['codigo']
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
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = ConsultoriosSerializer(objeto, data = request.data)        
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)

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
        del request.data['codigo']
        serializer = ConsultoriosSerializer(data=request.data)
        # request.data['codigo'] = '005'
        # return Response({'status': True,'message': request.data})
        if serializer.is_valid():
            # return Response({'status': True,'message': request.data})
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
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def MEDICOS_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Medicos.objects.all().order_by('-me_codigo')
        serializer = MedicosSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
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


## ===========================  LISTA DE FUNCIONES DE PROCESO   =========================== ##
## 1.- Función que genera Código Automatico
# def f_agregar_item_dicc(lista,key,valor):
#     ListReturn = list()
#     for items in lista:
#         items[key] = valor
#         ListReturn.append(items)