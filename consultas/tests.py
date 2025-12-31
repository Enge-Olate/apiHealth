from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import uuid

# IMPORTS CRUZADOS (Ajuste o caminho se necessário)
from .models import Consulta
from profissionais.models import Profissional
from paciente.models import Paciente

class ConsultaTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='123')
        refresh = RefreshToken.for_user(self.user)
        token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)        
        self.url_list = reverse('consulta-list')

        # 1. Criar dependências (Médico e Paciente)
        self.pro = Profissional.objects.create(
            nome="Dra. Teste", 
            crm="999", 
            especialidade="Geral"
        )
        self.pac = Paciente.objects.create(
            nome="Maria Teste", 
            cpf="99988877766",
            telefone='3588234322', 
            data_nascimento="1995-05-05"
        )

    def test_agendar_consulta(self):
        data_futura = (datetime.now() + timedelta(days=1)).isoformat()
        print(data_futura)
        self.dados = {
            "profissional": self.pro.id,
            "paciente": self.pac.id,
            "data": data_futura
        }
        response = self.client.post(self.url_list, self.dados, format='json')
        if response.status_code != 201:
            print(f"\n🚨 ERRO: {response.status_code}")
            print(f"Detalhes: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_erro_paciente_inexistente(self):
        """Tenta agendar para um UUID que não existe no banco"""
        dados = {
            "profissional": self.pro.id,
            "paciente": uuid.uuid4(), # ID aleatório
            "data": datetime.now().isoformat()
        }
        response = self.client.post(self.url_list, dados)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)