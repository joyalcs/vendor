from rest_framework import serializers
from .models import Vendor, HistoricalPerformance
from django.utils.translation import gettext as _


# Vendor
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"
        read_only_fields = ["vendor_id", "on_time_delivery_rate", "quality_rating_average", "average_response_time", "fulfillment_rate"]



class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
