from django.test import TestCase
from vendor.models import Vendor, HistoricalPerformance
from vendor.serializers import VendorSerializer, HistoricalPerformanceSerializer

class VendorSerializerTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address = 'Vendor street',
            vendor_id = 'vendorid12345',
            on_time_delivery_rate=0.75,
            quality_rating_average=4.0,
            average_response_time=35.0,
            fulfillment_rate=0.85
        )

    def test_vendor_serializer(self):
        '''Test for vendor serializer'''
        serializer = VendorSerializer(instance=self.vendor)

        self.assertEqual(serializer.data['name'], 'Test_Vendor')
        self.assertEqual(serializer.data['contact_details'], '123456789')
        self.assertEqual(serializer.data['address'], 'Vendor street')
        self.assertEqual(serializer.data['vendor_id'],'vendorid12345' )
        self.assertEqual(serializer.data['on_time_delivery_rate'], 0.75)
        self.assertEqual(serializer.data['quality_rating_average'], 4.0)
        self.assertEqual(serializer.data['average_response_time'], 35.0)
        self.assertEqual(serializer.data['fulfillment_rate'], 0.85)

class HistoricalPerformanceTest(TestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(
            name='Test_Vendor',
            contact_details='123456789',
            address = 'Vendor street',
            vendor_id = 'vendorid12345',
            on_time_delivery_rate=0.75,
            quality_rating_average=4.0,
            average_response_time=35.0,
            fulfillment_rate=0.85
        )

        self.historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            on_time_delivery_rate=0.75,
            quality_rating_average=4.0,
            average_response_time=35.0,
            fulfillment_rate=0.85
        )

    def test_historical_performance_serializer(self):
        '''Test for historical performance serializer'''
        serializer = HistoricalPerformanceSerializer(instance=self.historical_performance)
        self.assertEqual(serializer.data['vendor'], self.vendor.vendor_id)
        self.assertEqual(serializer.data['on_time_delivery_rate'], 0.75)
        self.assertEqual(serializer.data['quality_rating_average'], 4.0)
        self.assertEqual(serializer.data['average_response_time'], 35.0)
        self.assertEqual(serializer.data['fulfillment_rate'], 0.85)
