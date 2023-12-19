from django.test import TestCase
from django.utils import timezone
from order.models import PurchaseOrder
from vendor.models import Vendor
from order.constants import OrderStatus
from datetime import timedelta

class PurchaseOrderTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name="test_vendor",
            contact_details="1234567890",
            address="vendor street",
        )

    def test_create_purchase_order(self):
        '''Test for creating a purchase order'''
        order = PurchaseOrder.objects.create(
            vendor=self.vendor,
            items={"item1": "pen"},
            quantity=2,
            status=OrderStatus.PENDING,
            quality_rating=4.5,
        )
        self.assertIsInstance(order, PurchaseOrder)
        self.assertEqual(order.vendor, self.vendor)
        self.assertEqual(order.items, {"item1": "pen"})
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.status, OrderStatus.PENDING)
        self.assertEqual(order.quality_rating, 4.5)
