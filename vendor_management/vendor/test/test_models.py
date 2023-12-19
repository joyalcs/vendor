from django.test import TestCase
from django.utils import timezone
from  vendor.models import Vendor, HistoricalPerformance
from order.constants import OrderStatus
from rest_framework.test import APIClient
# from django.contrib.auth import get_user_model
from user.models import User
from order.models import PurchaseOrder

class VendorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email = "test@gmail.com",
            password="testpass"
        )
        self.client = APIClient()
        self.client.login(
            username='testuser',
            password='testpass'
        )

        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address = 'Vendor street'
        )

    def test_get_purchase_order_by_status(self):
        """Test for get_purchase_order_by_status method"""

        completed_order = PurchaseOrder.objects.create(
            status=OrderStatus.COMPLETED,
            acknowledge_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=1),
            items={"item1": 'testitem'},
            vendor=self.vendor
        )
        pending_order = PurchaseOrder.objects.create(
            status=OrderStatus.PENDING,
            acknowledge_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=1),
            items={"item1": 'testitem'},
            vendor=self.vendor
        )
        cancelled_order = PurchaseOrder.objects.create(
            status=OrderStatus.CANCELLED,
            acknowledge_date=timezone.now(),
            delivery_date=timezone.now() + timezone.timedelta(days=1),
            items={"item1": 'testitem'},
            vendor=self.vendor
        )

        '''Test for completed order'''
        completed_orders = self.vendor.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        self.assertEqual(completed_orders.count(), 1)
        self.assertEqual(completed_orders.first(), completed_order)

        '''Test for pending orders'''
        pending_orders = self.vendor.get_purchase_orders_by_status(status=OrderStatus.PENDING)
        self.assertEqual(pending_orders.count(), 1)
        self.assertEqual(pending_orders.first(), pending_order)

        '''Test for cancelled order'''
        canceled_orders = self.vendor.get_purchase_orders_by_status(status=OrderStatus.CANCELLED)
        self.assertEqual(canceled_orders.count(), 1)
        self.assertEqual(canceled_orders.first(), cancelled_order)

class HistoricalPerformanceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            email = "test@gmail.com",
            password="testpass"
        )
        self.client = APIClient()
        self.client.login(
            username='testuser',
            password='testpass'
        )

        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address = 'Vendor street',
            on_time_delivery_rate=0.8,
            quality_rating_average=4.5,
            average_response_time=30.0,
            fulfillment_rate=0.9
        )


    def test_performance_model(self):
        historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.75,
            quality_rating_average=4.0,
            average_response_time=35.0,
            fulfillment_rate=0.85
        )
        self.assertIsInstance(historical_performance, HistoricalPerformance)
        self.assertEqual(historical_performance.vendor, self.vendor)
        self.assertAlmostEqual(historical_performance.on_time_delivery_rate, 0.75, places=2)
        self.assertAlmostEqual(historical_performance.quality_rating_average, 4.0, places=2)
        self.assertAlmostEqual(historical_performance.average_response_time, 35.0, places=2)
        self.assertAlmostEqual(historical_performance.fulfillment_rate, 0.85, places=2)
