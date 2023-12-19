from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from vendor.models import Vendor, HistoricalPerformance
from vendor.serializers import VendorSerializer, HistoricalPerformanceSerializer
from user.models import User
from rest_framework.authtoken.models import Token

class VendorPerformanceViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email = "test@gmail.com",
            password="testpass"
        )

        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address = 'Vendor street'
        )

        self.historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.75,
            quality_rating_average=4.0,
            average_response_time=35.0,
            fulfillment_rate=0.85
        )
        self.client.force_authenticate(user=self.user)
    def test_list_vendors(self):
        """Test for vendors list"""
        url = reverse('vendors-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vendors(self):
        """Test for create vendor"""
        url = reverse('vendors-list')
        payload = {
            "name": "vendor1",
            "contact_details": "1234567890",
            "address": "test address"
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_vendor(self):
        """Test for retrieve a vendor"""
        url = f"/api/vendors/{self.vendor.vendor_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_vendor(self):
        """Test for update a vendor"""
        url = f"/api/vendors/{self.vendor.vendor_id}/"
        payload = {
            "name": "vendor1",
            "contact_details": "123456",
            "address": "test address"
        }
        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vendor(self):
        """Test for delete a vendor"""
        url = f"/api/vendors/{self.vendor.vendor_id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_vendor_performance(self):
        """Test for retrieve a vendor performance"""
        url = f'/api/vendors/{self.vendor.vendor_id}/performance/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
