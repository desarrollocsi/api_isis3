from rest_framework import status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Max

# Modelos
from Apps.Admision.citas.models import (
    Programacion,Citas,Medicos,Turnos)
# Serializadores
from .serializers import ProgramacionesListSerializer,ProgramacionSerializer

# Listar Programaciones por Fecha
class ProgramacionList(generics.ListCreateAPIView):
    serializer_class = ProgramacionesListSerializer
    def get_queryset(self):
        queryset = Programacion.objects.all()
        pfecha = self.request.query_params.get('fecha', None)
        if pfecha is not None:
            cfecha =  pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]
            queryset = queryset.filter(pr_fecha = cfecha,pr_estado = 'A').order_by('-pr_numero')
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
        except Medicos.DoesNotExist: 
            return Response({'status': False,'message': 'El "Médico" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        try: 
            ObjTurno        = Turnos.objects.get(tu_codigo = request.data['pr_turno']) 
        except Turnos.DoesNotExist: 
            return Response({'status': False,'message': 'El "Turno" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        request.data['pr_cupos']        = f_calcula_cupos(ObjTurno.tu_horas,ObjMedico.me_intervalo)
        request.data['pr_minutos']      = ObjMedico.me_intervalo
        request.data['pr_fecha']        = pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]
        request.data['pr_estado']        = 'A'
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
        objeto = Programacion.objects.all().order_by('-pr_numero')
        serializer = ProgramacionSerializer(objeto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pfecha = request.data['pr_fecha'] 
        pr_numero_max   = Programacion.objects.all().aggregate(Max('pr_numero'))['pr_numero__max']  or 0   
        request.data['pr_numero'] = str(int(pr_numero_max) +1).rjust(8,'0')
        try: 
            ObjMedico       = Medicos.objects.get(me_codigo = request.data['pr_medico'])
        except Medicos.DoesNotExist: 
            return Response({'status': False,'message': 'El "Médico" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        try: 
            ObjTurno        = Turnos.objects.get(tu_codigo = request.data['pr_turno']) 
        except Turnos.DoesNotExist: 
            return Response({'status': False,'message': 'El "Turno" seleccionado no Existe.'}, status=status.HTTP_404_NOT_FOUND)   
        request.data['pr_cupos']        = f_calcula_cupos(ObjTurno.tu_horas,ObjMedico.me_intervalo)
        request.data['pr_minutos']      = ObjMedico.me_intervalo
        request.data['pr_estado']       = 'A'
        request.data['pr_tipo']         = 'N'        
        request.data['pr_fecha']        = pfecha[-2:] +'/'+pfecha[5:7]+'/'+pfecha[:4]
        # return Response({'status': True,'message': request.data['pr_fecha'] })
        serializer = ProgramacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.'}, 
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




## ===========================  LISTA DE FUNCIONES DE PROCESO   =========================== ##

## 1.- Función que Calcula los cupos. Retorna Entero.
f_calcula_cupos = lambda horas,intervalo: int(((int(horas[0:2])*60) + int(horas[3:]))/intervalo)
