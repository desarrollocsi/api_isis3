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
        _url_ListaCta  = "https://integraciones.unilabs.pe/wssi" # Producción
        _url_Solicitud = "https://integraciones.unilabs.pe/wshospsi" # Producción Pruebas
        # datarequest = request.data
        respuesta = {}
        # return Response({'error': True, 'messaje': '1'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            _data = json.dumps(request.data)
            _url = _url_ListaCta
            if 'operation' in request.data:
                if 'valor' in request.data['operation']:
                    if request.data['operation']['valor'] == 'getSolicitud':
                        _url = _url_Solicitud
            _data = str(_data)
            # Convert string to byte
            _data = _data.encode('utf-8')
            req = rq.Request(url= _url, data=_data, headers={}, method='POST')    # • Consultando APi.
            response = rq.urlopen(req)                 # • Obteniendo Respuesta.
            string = response.read().decode('latin-1')
            string = string.replace('\n', ' ').replace('\r', '') # .replace(" ", "").replace(",}", "}")

        except HTTPError as http_err:
            respuesta = {'error': True,'messaje': http_err}
        except Exception as err:
            respuesta = {'error': True, 'messaje': err}
        else:
            respuesta = json.loads(string)
            items = list()
            if request.data['operation']['valor'] =='getListadoNroCta':
                if 'error' in respuesta:
                    if respuesta['error'] == 'OK':
                        for i in respuesta['listado']:
                            for j in i['lanalisis']:
                                items.append(j)
                        respuesta['items'] = items
        return Response(respuesta, status = response.status)
