from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Paciente

class PacienteTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='123')
        self.client.force_authenticate(user=self.user)
        
        self.url_list = reverse('paciente-list')
        self.dados = {
            "nome": "João Paciente",
            "cpf": "11122233344",
            "data_nascimento": "1990-01-01"
        }

    def test_criar_paciente(self):
        response = self.client.post(self.url_list, self.dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Paciente.objects.count(), 1)

    def test_cpf_unico(self):
        """Não deve permitir dois pacientes com mesmo CPF"""
        Paciente.objects.create(**self.dados)
        response = self.client.post(self.url_list, self.dados)
        print(f"Mesmo cpf: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)