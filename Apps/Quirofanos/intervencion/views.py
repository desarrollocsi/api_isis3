from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.intervencion import *
from .serializers import *


@api_view(['GET'])
def intervencion_api_view(request,pk):
     intervencions = Intervencion.objects.all()
     if request.method == 'GET':
         intervencions = intervencions.filter(se_codigo=pk)        
         Intervencion_serializers = IntervencionSerializers(intervencions,many=True)
         return Response(Intervencion_serializers.data)


@api_view(['GET'])
def intervencion_codigo_api_view(request,pk):
    intervencions = Intervencion.objects
    if request.method == 'GET':
        intervencions = intervencions.filter(cq_codiqx=pk).first()
        Intervencion_serializers = IntervencionSerializers(intervencions)
        return Response(Intervencion_serializers.data)