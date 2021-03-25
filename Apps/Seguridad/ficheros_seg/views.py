from django.shortcuts import render

from django.shortcuts import render
from rest_framework import viewsets
from ..menus.models import Rol
from ..menus.serializer import RolsSerializer


from rest_framework import status,generics,response

# Create your views here.
# JLT:2021-01-21 -- Listado de Vistas del Módulo Seguridad

class rolsViewSet(viewsets.ModelViewSet):
    serializer_class = RolsSerializer
    queryset    = Rol.objects.all()
