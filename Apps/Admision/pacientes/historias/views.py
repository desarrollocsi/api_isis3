from rest_framework import serializers, viewsets,status,generics #Vistas genéricas = "generics"
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Importando "Q" para condicional disyuntiva = "or".
from django.db.models import Q,F
# Importando "Concat" para concatenar campos
from django.db.models.functions import Concat
# Importando "Value" para concatenar campos VACIOS
from django.db.models import Value

# ** Modelos
from ..models import Historias
# ** Serializadores
from .serializers import HistorasSearchSerializer,HistoriasSerializer

from rest_framework.permissions import IsAuthenticated

from django.db.models import CharField, Value as V


## Listar Historias busqueda automatica.
class HistoriasSearchList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = HistorasSearchSerializer
    def get_queryset(self):
        buscar  = self.request.query_params.get('search', None)
        # queryset = Historias.objects.values('hc_apepat','hc_apemat','hc_nombre','hc_numhis','hc_sexo','hc_fecnac').annotate(nombrecompleto=Concat('hc_apepat', Value(' '), 'hc_apemat', Value(' '), 'hc_nombre'))
        # queryset = Historias.objects.annotate(nombrecompleto=Concat('hc_apepat', Value(' '), 'hc_apemat', Value(' '), 'hc_nombre'))
        queryset = Historias.objects.annotate(nombrecompleto=Concat('hc_apepat', V(' '), 'hc_apemat', V(' '),output_field=CharField()))
        if buscar is not None:
            queryset = queryset.filter(Q(nombrecompleto__istartswith = buscar.upper()),)
            # queryset = queryset.filter(Q(hc_numhis__contains = buscar) | Q(nombrecompleto__istartswith = buscar.upper()),)
            # .annotate(nombrecompleto=Concat('hc_apepat', Value(' '), 'hc_apemat', Value(' '), 'hc_nombre'))
        return queryset


"""
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■     HISTORIAS           ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
"""

@api_view(['GET', 'PUT', 'DELETE'])
def HISTORIAS_GPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    try:
        objeto = Historias.objects.get(hc_numhis=pk)
    except Historias.DoesNotExist:
        return Response({'status': False,'message': 'No se econtraron datos.'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET':
        respuesta = HistoriasSerializer(objeto)
        return Response(respuesta.data)
    elif request.method == 'PUT':
        serializer = HistoriasSerializer(objeto, data = request.data)
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
def HISTORIAS_GP(request):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar todos los datos o crear nuevo registro.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = Historias.objects.all().order_by('-hc_numhis')
        serializer = HistoriasSerializer(objeto, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['hc_numhis'] = f_generar_codigo("Historias","hc_numhis",10)
        request.data['hc_estado'] =  '00000001'
        request.data['idpaciente'] =  100
        serializer = HistoriasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'Registros grabados correctamente.','data': serializer.data}, status=status.HTTP_201_CREATED) 
            # return Response({'status': True,'message': 'Registros grabados correctamente.','data':serializers.data},
            # status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## ===========================  LISTA DE FUNCIONES DE PROCESO   =========================== ##

def f_generar_codigo(NomObj,NomCamp,largo):
    expresion = NomObj + ".objects.latest('"+NomCamp+"')."+NomCamp
    # rows =  Consultorios.objects.latest('co_codigo').co_codigo
    rows = eval(expresion)
    maximo = str(int(rows)+1)
    return str(maximo.zfill(largo))