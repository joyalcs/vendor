from django.db import models
from django.utils.translation import gettext as _
from shortuuid.django_fields import ShortUUIDField
from order.constants import OrderStatus
from django.db import models
from django.urls import reverse
from typing import Union
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=155)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_id = ShortUUIDField(
        length=10, max_length=20, prefix="ven", alphabet="abcdefg1234", primary_key=True
    )
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_average = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    def get_purchase_orders_by_status(
        self, status=Union[OrderStatus, str] | None
    ) -> models.QuerySet | None:
        "filter the purchase orders with the status"
        if status is None:
            return self.purchase_orders.all()
        elif OrderStatus.is_valid_status(status=status):
            return self.purchase_orders.filter(status=status)
        else:
            return None

    def calc_on_time_delivery_rate(self):
        """ Calculates the on time delivery dates"""
        purchase_order_list = self.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        res = purchase_order_list.filter(
            acknowledge_date__lte=models.F('delivery_date')
        )
        try:
            return round(res.count() / purchase_order_list.count(), 2)
        except ZeroDivisionError:
            return 0

    def calc_quality_rating_average(self):
        """Calculates the average rating on quality."""
        purchase_order_list = self.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        res = purchase_order_list.aggregate(
            quality_rating_average=models.Avg('quality_rating')
        )
        try:
            quality_rating_average = res.get('quality_rating_average')
            if quality_rating_average is not None:
                return round(quality_rating_average, 2)
            else:
                return 0
        except ZeroDivisionError:
            return 100


    def calc_average_response_time(self):
        """Calculates the average response time after Order is placed"""
        list = self.purchase_orders.filter(
            issue_date__isnull=False, acknowledge_date__isnull=False
        )

        if list.exists():
            res = list.aggregate(
                average_response_time=models.Avg(
                    models.F("acknowledge_date") - models.F("issue_date")
                )
            )
        try:
            # Convert timedelta to seconds and then round
            average_response_time_seconds = res.get('average_response_time').total_seconds()
            return round(average_response_time_seconds, 2)
        except ZeroDivisionError:
            return 0

    def calc_fulfillment_rate(self):
        """Calculate the fullfillment rate"""
        purchase_order_list_fulfilled = self.get_purchase_orders_by_status(status=OrderStatus.COMPLETED)
        purchase_order_list_not_fulfilled = self.get_purchase_orders_by_status(status=OrderStatus.PENDING)
        try:
            return round(purchase_order_list_fulfilled.count() / purchase_order_list_not_fulfilled.count(), 2)
        except ZeroDivisionError:
            return 100


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(
        Vendor, related_name="historical_performance", on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_average = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.vendor
