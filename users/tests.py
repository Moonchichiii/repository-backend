from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


# Create your tests here.


class UserTests(APITestCase):

    def create_user(self, username='testuser', email='tester2023@example.com', password='2023tester'):
        User.objects.create_user(
            username=username, email=email, password=password)

    def login_user(self, username='testuser', password='2023tester'):
        url = reverse('users:login')
        data = {'username': username, 'password': password}
        response = self.client.post(url, data, format='json')
        return response

    def test_user_creation(self):
        url = reverse('users:register')
        data = {
            'username': 'testuser',
            'email': 'tester2023@example.com',
            'password': '2023tester',
            'confirm_password': '2023tester'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(User.objects.get().username, 'testuser')

    def test_missing_fields(self):
        
        url = reverse('users:register')
        data = {'username': 'tester2023', 'password': '2023tester'}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_view(self):

        self.create_user()
        response = self.login_user()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_failed_login(self):

        url = reverse('users:login')
        data = {'username': '2023tester', 'password': 'tester2023'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
