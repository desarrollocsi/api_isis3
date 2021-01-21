from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from .models import Rols
from .serializers import RolsSerializer

from rest_framework import status,generics,response

# Create your views here.
# JLT:2021-01-21 -- Listado de Vistas del Módulo Seguridad

class rolsViewSet(viewsets.ModelViewSet):
    serializer_class = RolsSerializer
    queryset    = Rols.objects.all()
