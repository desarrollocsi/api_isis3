from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework import viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import Especialidades,Medicos,Programacion,Turnos,Consultorios
from .serializers import EspecialidadesSerializer,MedicosSerializer
from .serializers import TurnosSerializer,ProgramacionesSerializer,ConsultoriosSerializer

# Create your views here.
# class EspecialidadViewSet(viewsets.ModelViewSet):
#     queryset = Especialidades.objects.all().order_by('-es_codigo')
#     serializer_class = EspecialidadesSerializer

# class MedicosViewSet(viewsets.ModelViewSet):
#     queryset = Medicos.objects.all().order_by('-me_codigo')
#     serializer_class = MedicosSerializer

# class TurnosViewSet(viewsets.ModelViewSet):
#     queryset = Turnos.objects.all().order_by('-tu_codigo')
#     serializer_class = TurnosSerializer

# class ConsultoriosViewSet(viewsets.ModelViewSet):
#     queryset = Consultorios.objects.all().order_by('-co_codigo')
#     serializer_class = ConsultoriosSerializer
# -------------------------------   REQUEST DE VISTAS ---------------------------------------
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     ESPECIALIDADES      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

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
        return Response(respuesta.data) 
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
        objeto = Especialidades.objects.all()
        serializer = EspecialidadesSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EspecialidadesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     TURNOS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
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
        return Response(respuesta.data) 
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
        objeto = Turnos.objects.all()
        serializer = TurnosSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TurnosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     CONSULTORIOS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
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
        return Response(respuesta.data) 
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
        objeto = Consultorios.objects.all()
        serializer = ConsultoriosSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ConsultoriosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     MEDICOS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
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
        objeto = Medicos.objects.all()
        serializer = MedicosSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MedicosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MedicosList(generics.ListCreateAPIView):
    # 
    serializer_class = MedicosSerializer
    def get_queryset(self):
        queryset = Medicos.objects.all()
        idespecialidad = self.request.query_params.get('especialidad', None)     
        if idespecialidad is not None:
            queryset = queryset.filter(me_especialidad = idespecialidad)
        return queryset

class ProgramacionList(generics.ListCreateAPIView):
    serializer_class = ProgramacionesSerializer
    def get_queryset(self):
        queryset = Programacion.objects.all()
        pfecha = self.request.query_params.get('fecha', None)         
        if pfecha is not None:
            cfecha =  pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]  
            queryset = queryset.filter(pr_fecha = cfecha,pr_estado = 'A')
        return queryset

@api_view(['GET', 'POST'])
def pruebas(request):    
    if request.method == "GET":
        pfecha = request.query_params.get('fecha', None) 
        cfecha =  pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]  
        return JsonResponse({'prueba': cfecha}, status=status.HTTP_200_OK)

# class ProgramacionViewSet(viewsets.ModelViewSet):
#     queryset = Programacion.objects.all()
#     serializer_class = ProgramacionesSerializer

