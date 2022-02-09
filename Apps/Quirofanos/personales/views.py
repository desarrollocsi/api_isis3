from django.db.models import CharField, Value
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.personales import *
from .serializers import *


@api_view(['GET'])
def personales_api_view(request):
    if request.method == 'GET':
        personales = Personales.objects.values_list('pl_codper','pl_nombre').annotate(tipo=Value('A',output_field=CharField())).filter(pl_estado='1')
        medicos = Medicos.objects.values_list('me_codigo','me_nombres').annotate(tipo=Value('M',output_field=CharField())).filter(me_estado='A')
        key = ('codigo','nombre','tipo')
        data = []
        for value in personales.union(medicos):
            data.append(dict(zip(key,value)))
        data_serializer = PersonalSerializer(data,many=True)    
        return Response(data_serializer.data)
