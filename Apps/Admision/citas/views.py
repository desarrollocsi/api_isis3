from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework import viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
# Modelos
from Apps.Admision.citas.models import (
    Programacion,Citas,Medicos,Turnos,Cie10,Antecedentes,AntecedentesActoMedico,ActoMedico)
# Serializadores
from Apps.Admision.citas.serializers import (
    ProgramacionesListSerializer,MedicosSerializer,
    ProgramacionSerializer,CitasListSerializer,
    Cie10ListSerializer,AntecedentesListSerializer,
    AntecedentesAMSerializer,DiagnosticoAMSerializer,
    ActoMedicoSerializer,CitasSerializer)

from django.db.models import Max
from django.db.models import Q
from datetime import date

# Create your views here.

class ProgramacionList(generics.ListCreateAPIView):
    serializer_class = ProgramacionesListSerializer
    def get_queryset(self):
        queryset = Programacion.objects.all()
        pfecha = self.request.query_params.get('fecha', None)         
        if pfecha is not None:
            cfecha =  pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]  
            queryset = queryset.filter(pr_fecha = cfecha,pr_estado = 'A' )
        return queryset

class MedicosList(generics.ListCreateAPIView):
    serializer_class = MedicosSerializer
    def get_queryset(self):
        queryset = Medicos.objects.all()
        idespecialidad = self.request.query_params.get('especialidad', None)     
        if idespecialidad is not None:
            queryset = queryset.filter(me_especialidad = idespecialidad,me_estado = 'A').order_by('me_nombres')
        return queryset

class CitasList(generics.ListCreateAPIView):
    serializer_class = CitasListSerializer
    def get_queryset(self):
        queryset = Citas.objects.all()
        pfecha  = self.request.query_params.get('fecha', None)     
        pmedico = self.request.query_params.get('medico', None)
        dfecha  = pfecha[:4]+pfecha[5:7]+pfecha[-2:]
        if pfecha is not None and pmedico is not None:
            # print(queryset.filter(ci_fechacita = dfecha ,ci_medico = pmedico).query)
            # print(queryset.filter(ci_fechacita__date = pfecha,ci_medico = pmedico).query)
            print(date.today())
            data = queryset.filter(ci_fechacita__date = pfecha,ci_medico = pmedico,ci_estado__in = ['R','A']).order_by('ci_horatencion')
        return data


class Cie10List(generics.ListCreateAPIView):
    serializer_class = Cie10ListSerializer
    def get_queryset(self):
        queryset = Cie10.objects.all()
        buscar  = self.request.query_params.get('search', None)       
        if buscar is not None:
            queryset = queryset.filter(Q(codigo__icontains = buscar) | Q(descripcion__icontains = buscar) )
        return queryset

class AntecedentesList(generics.ListCreateAPIView):
    serializer_class = AntecedentesListSerializer
    def get_queryset(self):
        queryset = Antecedentes.objects.all()
        return queryset

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   CRUD  PROGRAMACION      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@api_view(['GET', 'PUT', 'DELETE'])
def PROGRAMACION_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try: 
        objeto = Programacion.objects.get(pr_numero=pk) 
    except Programacion.DoesNotExist: 
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        respuesta = ProgramacionSerializer(objeto) 
        return Response(respuesta.data) 
    elif request.method == 'PUT':
        pfecha = request.data['pr_fecha'] 
        try: 
            ObjMedico       = Medicos.objects.get(me_codigo = request.data['pr_medico'])
        except ObjMedico.DoesNotExist: 
            return Response({'status': False,'message': 'El "Médico" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        try: 
            ObjTurno        = Turnos.objects.get(tu_codigo = request.data['pr_turno']) 
        except ObjTurno.DoesNotExist: 
            return Response({'status': False,'message': 'El "Turno" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        request.data['pr_cupos']        = f_calcula_cupos(ObjTurno.tu_horas,ObjMedico.me_intervalo)
        request.data['pr_minutos']      = ObjMedico.me_intervalo
        request.data['pr_fecha']        = pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]
        serializer = ProgramacionSerializer(objeto, data = request.data)        
        if serializer.is_valid(): 
            serializer.save() 
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        if Citas.objects.filter(ci_programacion = pk).count() > 0:
            return Response({'status': False,'message': 'Existen Citas ya generadas con la programación.'},status=status.HTTP_400_BAD_REQUEST)
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def PROGRAMACION_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Programacion.objects.all().order_by('-me_codigo')
        serializer = ProgramacionSerializer(objeto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pfecha = request.data['pr_fecha'] 
        pr_numero_max   = Programacion.objects.all().aggregate(Max('pr_numero'))['pr_numero__max']       
        request.data['pr_numero']       = str(int(pr_numero_max)+1).rjust(8,'0')
        try: 
            ObjMedico       = Medicos.objects.get(me_codigo = request.data['pr_medico'])
        except ObjMedico.DoesNotExist: 
            return Response({'status': False,'message': 'El "Médico" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        try: 
            ObjTurno        = Turnos.objects.get(tu_codigo = request.data['pr_turno']) 
        except ObjTurno.DoesNotExist: 
            return Response({'status': False,'message': 'El "Turno" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        request.data['pr_cupos']        = f_calcula_cupos(ObjTurno.tu_horas,ObjMedico.me_intervalo)
        request.data['pr_minutos']      = ObjMedico.me_intervalo
        request.data['pr_estado']       = 'A'
        request.data['pr_tipo']         = 'N'
        request.data['pr_fecha']        = pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]
        serializer = ProgramacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   CRUD  ACTO MEDICO      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@api_view(['POST'])
def REGISTRE_ACTOMEDICO(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'POST':  
        idCita = request.data["idcita"]
        if ActoMedico.objects.filter(idcita = idCita).count() > 0:  
            return Response({'status': False,'message':'La cita ya cuenta con Acto Médico.'}) # Valida que la cita sea la unica.
        AntActMed       = f_agregar_item_dicc(request.data["antecedentes"],"idcita",idCita)
        DiaActMed       = f_agregar_item_dicc(request.data["diagnosticos"],"idcita",idCita)
        serializerAAM   = AntecedentesAMSerializer(data=AntActMed,many = True)
        serializerDAM   = DiagnosticoAMSerializer(data=DiaActMed,many = True)
        serializer      = ActoMedicoSerializer(data=request.data)

        ''' *************               VALIDACIONES            *************** '''
        if not serializerAAM.is_valid():    # si los datos de Antecedentes Médicos son correctos.
            return Response({'status': False,'message' :serializerAAM.errors}, status=status.HTTP_400_BAD_REQUEST)
        elif  not serializerDAM.is_valid(): # si los datos del Diagnóstico Médico son correctos.
            return Response({'status': False,'message' :serializerDAM.errors}, status=status.HTTP_400_BAD_REQUEST)
        elif  not serializer.is_valid():    # si los datos del Acto médico son correctos.
            return Response({'status': False,'message' :serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        ''' *************     REGISTRANDO   ACTO MEDICO    *************** '''
        serializer.save()
        ''' *************     REGISTRANDO ANTECEDENTES ACTO MEDICO    *************** '''
        serializerAAM.save()
        ''' *************     REGISTRANDO DIAGNOSTICOS ACTO MEDICO    *************** '''
        serializerDAM.save()
        ''' *************     ACTUALIZANDO EL ESTADO DE LA CITA   *************** '''
        Citas.objects.filter(ci_idcita=idCita).update(ci_estado= 'A')

        return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
        status=status.HTTP_201_CREATED)
        
## ===========================  LISTA DE FUNCIONES DE PROCESO   =========================== ##
## 1.- Función que genera lista para registrar
def f_agregar_item_dicc(lista,key,valor):
    ListReturn = list()
    for items in lista:
        items[key] = valor
        ListReturn.append(items)
    return ListReturn
## 2.- Función que Calcula los cupos. Retorna Entero.
f_calcula_cupos = lambda horas,intervalo: int(((int(horas[0:2])*60) + int(horas[3:]))/intervalo)


