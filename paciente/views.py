from rest_framework import viewsets
from .models import Paciente
from .serializers import SerialiserPaciente
# Create your views here.
class Pacienteviewset(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = SerialiserPaciente
    