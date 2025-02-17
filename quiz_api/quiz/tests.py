from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import QuizCategory

class QuizAPITestCase(APITestCase):

    def setUp(self):
        # Criar usuário para autenticação
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Obter token JWT
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpass'})
        self.token = response.data['access']

        # Configurar headers para autenticação
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Criar categoria de teste
        self.category = QuizCategory.objects.create(name="Ciência")

    def test_list_categories(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], "Ciência")

    def test_create_category(self):
        data = {"name": "História"}
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(QuizCategory.objects.count(), 2)

    def test_unauthenticated_access(self):
        self.client.credentials()  # Remove o token
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
