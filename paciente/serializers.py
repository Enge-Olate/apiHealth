from rest_framework import serializers
from .models import Paciente

class SerialiserPaciente(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields ='__all__'
