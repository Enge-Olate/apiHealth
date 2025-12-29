from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profissional
from rest_framework_simplejwt.tokens import RefreshToken

class ProfissionalTests(APITestCase):
    def setUp(self):
        # Autenticação
        self.user = User.objects.create_user(username='test_user', password='pass123')

        # self.client.force_authenticate(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)        
        self.url_list = reverse('profissional-list') # Verifique se o nome bate com seu router
        print(f"url: {self.url_list}")
        
        self.dados = {
            "nome": "Dr. Teste",
            "crm": "12345",
            "especialidade": "Cardio"
        }

    def test_criar_profissional(self):
        response = self.client.post(self.url_list, self.dados)

        if response.status_code != 201:
            print(f"foi para: {response.status_code}")

        if response.status_code == 401:
            print(f"{response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profissional.objects.count(), 1)

    def test_crm_unico(self):
        """Não deve permitir dois médicos com mesmo CRM"""
        Profissional.objects.create(**self.dados)
        response = self.client.post(self.url_list, self.dados) # Tenta criar de novo
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)