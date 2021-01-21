from django.shortcuts import render
from rest_framework import viewsets
from .models import formularioc
from .serializers import formularioSerializer

from rest_framework import status,generics
from django.http.response import JsonResponse

# Create your views here.
class formulariocViewSet(viewsets.ModelViewSet):
    serializer_class = formularioSerializer
    queryset    = formularioc.objects.all()

