from rest_framework import serializers
from .models import Profissional

class SerialiserProfissional(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'