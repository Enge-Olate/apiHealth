from rest_framework import serializers
from .models import Consulta

class SerializerConsulta(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'