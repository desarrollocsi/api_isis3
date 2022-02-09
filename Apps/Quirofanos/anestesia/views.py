from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
# 
from ..models.anestesia import *
from .serializers import *


@api_view(['GET'])
def anestesia_api_view(request):
     if request.method == 'GET':
         anestesia = Anestesia.objects.all().filter(an_estado='1')
         Anestesia_serializers = AnestesiaSerializers(anestesia,many=True)
         return Response(Anestesia_serializers.data)
