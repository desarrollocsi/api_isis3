from django.db import models
from django.views import generic
from rest_framework import viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Importando "Q" para condicional disyuntiva = "or".
from django.db.models import Q

# Importando la Count para agrupar registros.
from django.db.models import Count

# Modelos
from Apps.Admision.citas.models import (Programacion,Especialidades,Medicos,PlantillaAgenda,
    Citas,Cie10,ActoMedico,AntecedentesActoMedico,DiagnosticoActoMedico)
from Apps.Admision.pacientes.models import PlanesHistoria

# Serializadores
from Apps.Admision.citas.agendamedica.serializers import (EspecialidadesProgSerializer,
    ProgMedTurSerializer,AgendaMedicaSerializer,CitasListSerializer,AntecedentesAMSerializer,
    DiagnosticoAMSerializer,ActoMedicoSerializer,ActoMedicoListSerializer,IafasSerializer,CitasSerializer)

from Apps.Admision.ficheros.serializers import MedicosSerializer,Cie10ListSerializer



# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   LISTADO Y CRUD "AGENDAMEDICA"      ■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

## Listar las Especialidades por fecha de Programación
class EspeciliadadProgramacionList(generics.ListCreateAPIView):
    serializer_class = EspecialidadesProgSerializer
    def get_queryset(self):
        queryset = Especialidades.objects.all()
        pfecha = self.request.query_params.get('fecha', None)
        if pfecha is not None:
            cfecha =  pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]
            queryset = queryset.filter(pr_servicio__pr_fecha = cfecha ,pr_servicio__pr_estado = 'A').values('es_codigo','es_descripcion').annotate(total=Count('es_codigo'))
        return queryset
## Listar los Medicos por fecha de Programación
class MedicosProgramacionList(generics.ListCreateAPIView):
    serializer_class = ProgMedTurSerializer
    def get_queryset(self):
        queryset = Programacion.objects.all()
        pFecha = self.request.query_params.get('fecha', None)
        pEspecialidad = self.request.query_params.get('especialidad', None)
        if pFecha is not None:
            cfecha =  pFecha[-2:] +'/'+pFecha[5:7]+'/'+pFecha[:4]
            queryset = queryset.filter(pr_fecha = cfecha,pr_servicio = pEspecialidad,pr_estado = 'A')#.values('me_codigo','me_nombres','pr_medico__pr_turno__tu_tipoturno')
        return queryset

## Listar la Agenda Médica.
class AgendaMedicaListView(ListAPIView):
    serializer_class = AgendaMedicaSerializer
    def list(self, request):
        pProgramacion = self.request.query_params.get('programacion', None) 
        queryset = PlantillaAgenda.objects.raw("select orden,hora,horalleg,historia,paciente,cuenta,telefono,controla, \
        fecha,observaciones,titular,idcita,atend,telefono2,cond_serv  \
        from i3_ad_generar_plantilla(%s)",params=[pProgramacion])
        serializer = AgendaMedicaSerializer(queryset, many=True)
        return Response(serializer.data)

## Listar las Aseguradoras por Historia.
class IafasListView(ListAPIView):
    serializer_class = IafasSerializer
    def list(self, request):
        pHistoria = self.request.query_params.get('historia', None) 
        queryset = PlanesHistoria.objects.raw("select h.pl_desaseg,t.ta_codi tipoaseg,ta_acredita,h.id \
        from tipo_asegurado t \
        inner join planes_historia h \
        on to_number(t.ta_codi,'99999')=h.pl_codplan and t.ta_flag='1'  \
        where pl_numhist = %s and h.pl_estado = 1 order by h.pl_codaseg ",params=[pHistoria])
        # ,params=[pHistoria]
        # queryset = PlanesHistoria.objects.raw("select id,pl_desaseg from planes_historia where id = 22518")
        # print(queryset.query)
        serializer = IafasSerializer(queryset,many=True)
        return Response(serializer.data)




# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   LISTADO  "ACTO MEDICO"      ■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

## Listar Médicos por especialidad.
class MedicosList(generics.ListCreateAPIView):
    serializer_class = MedicosSerializer
    def get_queryset(self):
        queryset = Medicos.objects.all()
        idespecialidad = self.request.query_params.get('especialidad', None)
        if idespecialidad is not None:
            queryset = queryset.filter(me_especialidad = idespecialidad,me_estado = 'A').order_by('me_nombres')
        return queryset

## Listar Pacientes Citados.
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
            data = queryset.filter(ci_fechacita__date = pfecha,ci_medico = pmedico,ci_estado__in = ['R','A']).order_by('ci_horatencion')
        return data


## Listar Cie10 busqueda automatica.
class Cie10List(generics.ListCreateAPIView):
    serializer_class = Cie10ListSerializer
    def get_queryset(self):
        queryset = Cie10.objects.all()
        buscar  = self.request.query_params.get('search', None)
        if buscar is not None:
            queryset = queryset.filter(Q(codigo__icontains = buscar) | Q(descripcion__icontains = buscar) )
        return queryset

## Listar Acto Médico por Citas.
# class ActoMedicoList(generics.ListAPIView):
#     serializer_class = ActoMedicoListSerializer
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = ActoMedico.objects.all()
#         idcita = self.request.query_params.get('idcita')
#         if idcita is not None:
#             queryset = queryset.filter(id=idcita)
#             return queryset
#         else:
#             return Response({'status':False,'mensage':'Falta identificar el "idcita". '})

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   CRUD  "ACTO MEDICO"      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@api_view(['GET', 'PUT', 'DELETE'])
def ACTOMEDICO_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try:
        objeto = ActoMedico.objects.get(id=pk)
    except ActoMedico.DoesNotExist:
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        respuesta = ActoMedicoListSerializer(objeto)
        return Response(respuesta.data)
    elif request.method == 'PUT':
        idCita = request.data["idcita"]
        ''' *************               SERIALIZANDO EL OBJETO PARA EL REGISTRO            *************** '''
        serializer      = ActoMedicoSerializer(objeto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}, status=status.HTTP_201_CREATED)
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)


## CRUD ACTO MEDICO.
@api_view(['POST'])
def REGISTRE_ACTOMEDICO(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'POST':
        idCita = request.data["idcita"]
        ObjCitas = Citas.objects.filter(ci_idcita=idCita)
        if ObjCitas.count() <= 0:
            return Response({'status': False,'message':'No existe Cita!!.'}) # Valida que la cita sea la unica.
        serializer      = ActoMedicoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data_result =serializer.save()
            ObjCitas.update(ci_estado= 'A',actomedico_id = data_result.id)
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
## 1.- Función que genera lista para registrar
def f_agregar_item_dicc(lista,key,valor):
    ListReturn = list()
    for items in lista:
        items[key] = valor
        ListReturn.append(items)
    return ListReturn

##---------------------------------------------------##
## ----------------PRUEBAS---------------------------##
##---------------------------------------------------##

# class AgendaMedicaListView(ListAPIView):
#     queryset = PlantillaAgenda.objects.raw("select * from i3_ad_generar_plantilla('00060073')")
#     serializer_class = AgendaMedicaSerializer
#     def list(self, request):
#         queryset = self.get_queryset()
#         # print(queryset.query)
#         # the serializer didn't take my RawQuerySet, so made it into a list
#         serializer = AgendaMedicaSerializer(list(queryset), many=True)
#         return Response(serializer.data)




# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   CRUD  CITAS      ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
@api_view(['GET', 'PUT', 'DELETE'])
def CITAS_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try:
        objeto = Citas.objects.get(ci_idcita=pk)
    except Citas.DoesNotExist:
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        respuesta = CitasSerializer(objeto)
        return Response(respuesta.data)
    elif request.method == 'PUT':
        serializer = CitasSerializer(objeto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros actualizados correctamente.'}) 
        return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        objeto.delete()
        return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def CITAS_GP(request):

    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Citas.objects.all().order_by('-ci_idcita')
        serializer = CitasSerializer(objeto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            ObjProgramacion = Programacion.objects.get(pr_numero = request.data['ci_programacion'])
        except Programacion.DoesNotExist:
            return Response({'status': False,'message': 'La Programación seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)
        if Citas.objects.filter(ci_programacion = request.data['ci_programacion'],ci_orden=request.data['ci_orden']).exclude(ci_estado = "E").exists():
            return Response({'status': False,'message': 'Ya existe cita en ese Horario, registre otro horario.'}, status=status.HTTP_404_NOT_FOUND)     
        request.data['ci_servicio'] = ObjProgramacion.pr_servicio.es_codigo
        request.data['ci_turno'] = ObjProgramacion.pr_turno.tu_codigo
        request.data['ci_medico'] = ObjProgramacion.pr_medico.me_codigo
        request.data['ci_consultorio'] = ObjProgramacion.pr_consultorio.co_codigo
        request.data['ci_indicatencion']  = 'P'
        request.data['ci_estado'] = 'R'
        request.data['ci_atend'] = 0
        request.data['ci_tarifaExamen']  = 'CA'
        # return Response({'status': True,'message': request.data['pr_fecha'] })
        serializer = CitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)