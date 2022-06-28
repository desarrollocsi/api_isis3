from django.shortcuts import render
from rest_framework import viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     CENTROS DE COSTO      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def CENTROCOSTO_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = CentroCosto.objects.get(codigo=pk) 
    except CentroCosto.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = CentroCostoSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        del respuestadata['usuario']
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = CentroCostoSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def CENTROCOSTO_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = CentroCosto.objects.all().order_by('descr')
        serializer = CentroCostoSerializer(objeto, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CentroCostoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     MEDIOS DE PAGO      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def MEDIOPAGO_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = MedioPago.objects.get(mediopagoid=pk) 
    except MedioPago.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = MedioPagoSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = MedioPagoSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def MEDIOPAGO_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = MedioPago.objects.all().order_by('mediopagocodigo')
        serializer = MedioPagoSerializer(objeto, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MedioPagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     TIPO COMPROBANTE      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""
@api_view(['GET', 'PUT', 'DELETE'])
def TIPOCOMPROBANTE_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = TipoComprobante.objects.get(cm_tipcom=pk) 
    except TipoComprobante.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = TipoComprobanteSerializer(objeto) 
        respuestadata = respuesta.data.copy()
        return Response(respuestadata) 
    elif request.method == 'PUT':
        serializer = TipoComprobanteSerializer(objeto, data = request.data)     
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def TIPOCOMPROBANTE_GP(request):    
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = TipoComprobante.objects.all().order_by('cm_tipcom')
        serializer = TipoComprobanteSerializer(objeto, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoComprobanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
