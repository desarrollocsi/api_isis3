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

class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidades.objects.all().order_by('-es_codigo')
    serializer_class = EspecialidadesSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all().order_by('-me_codigo')
    serializer_class = MedicosSerializer

class TurnosViewSet(viewsets.ModelViewSet):
    queryset = Turnos.objects.all().order_by('-tu_codigo')
    serializer_class = TurnosSerializer

class ConsultoriosViewSet(viewsets.ModelViewSet):
    queryset = Consultorios.objects.all().order_by('-co_codigo')
    serializer_class = ConsultoriosSerializer

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

