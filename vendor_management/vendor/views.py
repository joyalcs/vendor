from django.shortcuts import render
from rest_framework import generics
from .models import Vendor, HistoricalPerformance
from .serializers import (
    VendorSerializer,
    HistoricalPerformanceSerializer,
)
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.


class VendorListView(generics.ListCreateAPIView):
    """View for creating a Vendor"""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for Retrieve, update and delete a vendor"""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = "vendor_id"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VendorPerformanceView(generics.RetrieveAPIView):
    """View for Retrieve Performance of a Vendor"""
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self):
        vendor_id = self.kwargs.get("vendor_id")
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        performance = vendor.historical_performance.last()
        return performance
