from rest_framework import viewsets
from django.shortcuts import render
from .models import Profissional
from .serializers import SerialiserProfissional
# Create your views here.
class ProfissionalViewset(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = SerialiserProfissional

