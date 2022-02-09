from Apps.Reclamos.models import (Clasificacion, Reclamos, Servicio, Tipo_documento, Estado, Resultado, Etapa, MedioRecepcion, Medidas, MotConcAnt, Tramas)
from .serializers import (ClasificacionSerializer, ReclamosSerializer, ReclamosSerializerData, MedioRecepcionSerializer, ReclamosSerializerList,
ServicioSerializer, TipoDocumentoSerializer, MedidasSerializer, EstadoSerializer, ResultadoSerializer, EtapaSerializer, MotConcAntSerializer,
TramaSerializer)
from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import F, Q
from django.shortcuts import get_object_or_404
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.

class EstadoList(generics.ListCreateAPIView):
    serializer_class = EstadoSerializer
    def get_queryset(self):
        queryset = Estado.objects.all().order_by('er_cod')
        return queryset

class EtapaList(generics.ListCreateAPIView):
    serializer_class = EtapaSerializer
    def get_queryset(self):
        queryset = Etapa.objects.all().order_by('etr_cod')
        return queryset

class ResultadoList(generics.ListCreateAPIView):
    serializer_class = ResultadoSerializer
    def get_queryset(self):
        queryset = Resultado.objects.all().order_by('rr_cod')
        return queryset

class TipoDocumetoList(generics.ListCreateAPIView):
    serializer_class = TipoDocumentoSerializer
    def get_queryset(self):
        queryset = Tipo_documento.objects.all().order_by('td_cod')
        return queryset

class ClasificacionList(generics.ListCreateAPIView):
    serializer_class = ClasificacionSerializer
    def get_queryset(self):
        queryset = Clasificacion.objects.all().order_by('cr_cod')
        return queryset

class ServicioList(generics.ListCreateAPIView):
    serializer_class = ServicioSerializer
    def get_queryset(self):
        queryset = Servicio.objects.all().order_by('sr_cod')
        return queryset

class MedioList(generics.ListCreateAPIView):
    serializer_class = MedioRecepcionSerializer
    def get_queryset(self):
        queryset = MedioRecepcion.objects.all().order_by('mr_cod')
        return queryset

class MotConcAntList(generics.ListCreateAPIView):
    serializer_class = MotConcAntSerializer
    def get_queryset(self):
        queryset = MotConcAnt.objects.all().order_by('mc_cod')
        return queryset

class ReclamosList(generics.ListCreateAPIView):
    queryset = Reclamos.objects.all().order_by('-periodo','-fecha')
    serializer_class = ReclamosSerializerList
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombres_p','paterno_p','materno_p','nro_documento_p','nombres','paterno','materno','nro_documento','periodo','fecha']

## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   RECLAMOS   ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

@api_view(['GET', 'PUT','POST', 'DELETE'])
def RECLAMO_GPPD(request, pk):
    """""""""""""""""""""""""""""""""""""""""""""""
    Listar ,Actualizar o Eliminar registros.
    """""""""""""""""""""""""""""""""""""""""""""""
    if request.method == 'GET':
        objeto = get_object_or_404(Reclamos, re_cod=pk)
        respuesta = ReclamosSerializerData(objeto)
        respuestadata = respuesta.data.copy()
        return Response(respuestadata)

    elif request.method == 'PUT':
        if Tramas.objects.filter(periodo = request.data['periodo']).count() > 0:
            return Response({'status': False,'message': 'Ya existe la trama del periodo, no puede actualizar los datos.'})
        else:
            objeto = get_object_or_404(Reclamos, re_cod=pk)
            serializer = ReclamosSerializer(objeto, data = request.data)
            if serializer.is_valid():
                objReclamos = serializer.save()
                Medidas.objects.filter(re_cod=pk).delete()
                if request.data["resultado"] in [1,2]:
                    ListReturn = list()
                    correlativo = 1
                    for items in request.data["medidas"]:
                        items['re_cod'] = objReclamos.re_cod
                        items['numero'] = correlativo
                        correlativo = correlativo + 1
                        ListReturn.append(items)
                    serializerMedidas = MedidasSerializer(data=ListReturn,many = True)
                    if serializerMedidas.is_valid():
                        serializerMedidas.save()
                        return Response({'status': True,'message': 'Registro grabado correctamente.'}, status=status.HTTP_201_CREATED)
                    else:
                        return Response(serializerMedidas.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'status': True,'message': 'Registro grabado correctamente.'}, status=status.HTTP_201_CREATED)
            return Response({'status': False,'message': serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        if Tramas.objects.filter(periodo =  request.data['periodo']).count() > 0:
            return Response({'status': False,'message': 'Ya existe la trama del periodo, no puede agregar más registros.'})
        else:
            del request.data['re_cod']
            serializer = ReclamosSerializer(data=request.data)
            if serializer.is_valid():
                objReclamos = serializer.save()
                ListReturn = list()
                correlativo = 1
                for items in request.data["medidas"]:
                    items['re_cod'] = objReclamos.re_cod
                    items['numero'] = correlativo
                    correlativo = correlativo + 1
                    ListReturn.append(items)
                serializerMedidas = MedidasSerializer(data=ListReturn,many = True)
                if serializerMedidas.is_valid():
                    serializerMedidas.save()
                    return Response({'status': True,'message': 'Registro grabado correctamente.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(serializerMedidas.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     objeto = Reclamos.objects.get(re_cod=pk)
    #     objeto.delete()
    #     return Response({'status': True,'message': 'Registros eliminados correctamente.'},status=status.HTTP_204_NO_CONTENT)


## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   TRAMAS   ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

@api_view(['GET','POST'])
def TRAMAS_GP(request, _periodo):
    if request.method == 'GET':
        objeto = Tramas.objects.all().filter(periodo = _periodo)
        if objeto:
            serializer = TramaSerializer(objeto, many=True)
            return Response(serializer.data)
        else:
            objeto = Reclamos.objects.all().filter(periodo = _periodo)
            serializer = ReclamosSerializerData(objeto, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        periodo = request.data['periodo']
        periodo_ant = datetime.strptime(periodo,'%Y%m') - relativedelta(months=1)
        if Tramas.objects.all().filter(periodo = periodo_ant.strftime('%Y%m')):
            serializer = TramaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                sig_periodo = datetime.strptime(periodo,'%Y%m') + relativedelta(months=1)
                Reclamos.objects.filter(Q(periodo=periodo) & Q(estado__in=[0, 2, 3])).update(periodo = sig_periodo.strftime('%Y%m'))
                return Response({'status': True,'message': 'Registro grabado correctamente.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': False,'message': 'Falta generar el la trama del periodo anterior.'}, status=status.HTTP_406_NOT_ACCEPTABLE)



