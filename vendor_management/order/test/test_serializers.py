from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from django.utils import timezone
from order.models import PurchaseOrder
from order.serializers import PurchaseOrderSerializer, AcknowledgeSerializer
from order.constants import OrderStatus
from vendor.models import Vendor

class PurchaseOrderSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email="test@gmail.com",
            password="testpass"
        )
        self.client.force_authenticate(user=self.user)
        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address='Vendor street'
        )
        self.purchase_orders = PurchaseOrder.objects.create(
            vendor=self.vendor,
            items={"item1": "pen"},
            quantity=2,
            status=OrderStatus.PENDING,
            quality_rating=4.5,
        )

    def test_purchase_order_serializer(self):
        serializer = PurchaseOrderSerializer(instance=self.purchase_orders)
        self.assertEqual(serializer.data['vendor'], self.vendor.vendor_id)
        self.assertEqual(serializer.data['items'], {"item1": "pen"})
        self.assertEqual(serializer.data['quantity'], 2)
        self.assertEqual(serializer.data['status'], OrderStatus.PENDING)
        self.assertEqual(serializer.data['quality_rating'], 4.5)

    def test_acknowledge_serializer(self):
        data = {"acknowledge_date": timezone.now()}
        serializer = AcknowledgeSerializer(instance=self.purchase_orders, data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()
