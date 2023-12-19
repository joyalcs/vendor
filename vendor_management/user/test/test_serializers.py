from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

class RegisterSerializerTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.valid_payload = {
            "username": "example_user",
            "password": "secure_password",
            "email": "user@example.com"
        }


    def test_valid_registration(self):
        """Test for a valid user registration."""
        response = self.client.post(self.register_url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_registration(self):
        """Test for an invalid user registration."""
        invalid_payload = {
            'username': 'testuser',
            'email': 'testemail',
            'password': 'testpass'
        }
        response = self.client.post(self.register_url, data=invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
