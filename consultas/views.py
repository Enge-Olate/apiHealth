from rest_framework import viewsets
from .serializers import SerializerConsulta
from .models import Consulta
# Create your views here.
class ConsultaViewset(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = SerializerConsulta