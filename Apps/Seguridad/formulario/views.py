from django.shortcuts import render
from rest_framework import viewsets
from .models import formularioc
from .serializers import formulariocSerializer,formularioSerializer

# Create your views here.
class formularioViewSet(viewsets.ModelViewSet):
    serializer_class = formularioSerializer
    queryset    = formularioc.objects.all()

class formulariocViewSet(viewsets.ModelViewSet):
    queryset = formularioc.objects.all().order_by('id')
    serializer_class = formulariocSerializer