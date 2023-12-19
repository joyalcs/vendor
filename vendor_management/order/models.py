from datetime import timedelta
from django.db import models
from .constants import OrderStatus
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from vendor.models import Vendor


# Create your models here.
class PurchaseOrder(models.Model):
    status_choices= (
        (OrderStatus.PENDING, "pending"),
        (OrderStatus.COMPLETED, "completed"),
        (OrderStatus.CANCELLED, "cancelled"),
    )
    po_id = ShortUUIDField(
        length=10, max_length=20, prefix="ord", alphabet="abcdefg1234", primary_key=True
    )
    vendor = models.ForeignKey(
        Vendor, related_name="purchase_orders", on_delete=models.CASCADE
    )
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(default=timezone.now() + timedelta(days=1))
    items = models.JSONField()
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=200, choices=status_choices, default=OrderStatus.PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledge_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_id

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
