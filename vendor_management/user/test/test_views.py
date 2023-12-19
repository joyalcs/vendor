from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserRegisterViewTest(APITestCase):
    def test_user_register_success(self):
        url = reverse('register')
        payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com"
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().username, 'testuser')

    def test_user_register_failure(self):
        url = reverse('register')
        payload = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(get_user_model().objects.count(), 0)
class CustomAuthTokenTest(APITestCase):

    def setUp(self):
        self.payload = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com"
        }
        self.user = get_user_model().objects.create_user(**self.payload)

    def test_custom_auth_token_success(self):
        url = reverse('custom-auth-token')
        payload = {
            "username": "testuser",
            "password": "testpassword"
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)



    def test_custom_auth_token_failure(self):
        url = reverse('custom-auth-token')
        payload = {
            "username": "testuser",
            "password": "wrongpassword"
        }

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response.data)
