from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from user.models import User
from order.models import PurchaseOrder
from order.constants import OrderStatus
from django.utils import timezone
from django.urls import reverse
from vendor.models import Vendor

class PurchaseOrderViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email = "test@gmail.com",
            password="testpass"
        )
        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address = 'Vendor street'
        )
        self.purchase_orders = PurchaseOrder.objects.create(
            vendor=self.vendor,
            items={"item1": "pen"},
            quantity=2,
            status=OrderStatus.PENDING,
            quality_rating=4.5,
            po_id="ord1234"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_Purchase_orders(self):
        """Test for purchase order list"""
        url = reverse('orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_Purchase_order(self):
        """Test for create Purchase Orders"""
        url = reverse('orders')
        payload = {
            "vendor": self.vendor.vendor_id,
            "po_id": "ord1234",
            "items": {"item1": "pen"},
            "quantity": 2,
            "status": OrderStatus.PENDING,
            "quality_rating": 4.5
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_order(self):
        """Test for retrieve a order"""
        url = f"/api/purchase_orders/{self.purchase_orders.po_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        """Test for update a order"""
        url = f"/api/purchase_orders/{self.purchase_orders.po_id}/"
        payload = {
            "vendor": self.vendor.vendor_id,
            "po_id": "ord1234",
            "items": {"item1": "pen"},
            "quantity": 3,
            "status": OrderStatus.PENDING,
            "quality_rating": 4.5
        }
        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        """Test for delete a vendor"""
        url = f"/api/purchase_orders/{self.purchase_orders.po_id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_acknowledge_order(self):
        url = f"/api/purchase_orders/{self.purchase_orders.po_id}/"
        url = f"/api/vendors/{self.vendor.vendor_id}/"
        payload = {
            "acknowledge_date": timezone.now()
        }
        response = self.client.patch(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
