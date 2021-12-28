# Modelos :
from ...citas.models import Citas
from ..models import Historias
# Serializadores :
from .serializers import CitasSerializer

from rest_framework.decorators import api_view
from rest_framework import generics

from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from django.db.models import Q

from django.db.models.functions import Concat
from django.db.models import F, Count, Value



## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■                        OBTENER CITAS POR DNI         ■■■■■■■■■■■■■■■
## ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# -------------------   version 1 ------------------------------------#
def consultacitas(request,id):
    if id is not None:
        Cita  = Citas.objects.filter(ci_numhist = id, ci_estado='A').order_by('ci_idcita') 
        if len(Cita)>0 :        
            serializer = CitasSerializer(Cita, many=True)
            return JsonResponse(serializer.data, safe=False,status=status.HTTP_200_OK)
        else:
            return JsonResponse({'status':False,'message':'No se obtuvieron datos'}, status=status.HTTP_200_OK) 
    else:            
        return JsonResponse({'status':False,'message':'DNI es necesario'},status=status.HTTP_200_OK)


class AtencionesListView(generics.ListAPIView):
    serializer_class = CitasSerializer
    def get_queryset(self):
        queryset = Citas.objects.all()
        buscar  = self.request.query_params.get('search', None)
        if buscar is None:
            return Response({'status':False,'message':'No se identifico "search"'})
        else:
            queryset = queryset.annotate(search_name=Concat('ci_numhist__hc_apepat', Value(' '), 'ci_numhist__hc_apemat', Value(' '), 'ci_numhist__hc_nombre'))
            queryset = queryset.filter(Q(search_name__icontains=buscar) | Q(ci_numhist__hc_numhis__icontains = buscar ) )
        return queryset
            # queryset = queryset.filter(Q(hc_numhis = buscar) | Q(descripcion__icontains = buscar) )



# class Cie10List(generics.ListCreateAPIView):
#     serializer_class = Cie10ListSerializer
#     def get_queryset(self):
#         queryset = Cie10.objects.all()
#         buscar  = self.request.query_params.get('search', None)       
#         if buscar is not None:
#             queryset = queryset.filter(Q(codigo__icontains = buscar) | Q(descripcion__icontains = buscar) )
#         return queryset