from django.shortcuts import render
from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer, AcknowledgeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class PurchaseOrderView(generics.ListCreateAPIView):
    """View for creating a purchase order"""

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """View for Retrieve, update and delete an Purchase order"""

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "po_id"


class AcknowledgePurchaseOrderView(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = AcknowledgeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "po_id"
