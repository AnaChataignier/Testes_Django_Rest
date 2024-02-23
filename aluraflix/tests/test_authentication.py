from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("programas-list")
        self.user = User.objects.create_user("aninha", password="280404")

    def test_authentication(self):
        """Teste verifica a autenticação de um user com as credenciais corretas"""
        user = authenticate(username="aninha", password="280404")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_nao_autorizada(self):
        """Teste que verifica uma requisição GET sem autenticar"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_username_incorreto(self):
        user = authenticate(username="ana", password="280404")
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_password_incorreto(self):
        user = authenticate(username="aninha", password="2804")
        self.assertFalse((user is not None) and user.is_authenticated)

    def teste_requisicao_user_autenticado(self):
        """Teste que verifica a requisição GET de um user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
