from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from urllib import request as rq
from urllib.error import HTTPError
import json

# Create your views here.
class UnilabsView(APIView):
    def post(self,request):
        # url = "https://integraciones.unilabs.pe/wsihosp" # Beta
        _url = "https://integraciones.unilabs.pe/wssi" # Producción
        # datarequest = request.data
        respuesta = {}
        # return Response({'error': True, 'messaje': '1'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            _data = json.dumps(request.data)
            _data = str(_data)
            # Convert string to byte
            _data = _data.encode('utf-8')
            req = rq.Request(url=_url, data=_data, headers={}, method='POST')    # • Consultando APi.
            response = rq.urlopen(req)                  # • Obteniendo Respuesta.
            string = response.read().decode('latin-1')
            string = string.replace('\n', ' ').replace('\r', '') # .replace(" ", "").replace(",}", "}")
        except HTTPError as http_err:
            respuesta = {'error': True,'messaje': http_err}
        except Exception as err:
            respuesta = {'error': True, 'messaje': err}
        else:
            respuesta = json.loads(string)
        return Response(respuesta, status=status.HTTP_200_OK)
