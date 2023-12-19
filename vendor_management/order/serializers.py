from rest_framework import serializers
from .models import PurchaseOrder
from . import signals
from django.utils import timezone
from django.utils.translation import gettext as _
from .constants import OrderStatus

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"
        read_only_fields = ["po_id"]
        extra_kwargs = {
            "order_date": {
                "error_messages": {"required": _("order date is must")}
            },
            "delivery_date": {
                "error_messages": {"required": _("delivery date is must")}
            },
            "quantity": {
                "error_messages": {"required": _("quantity is must")}
            },
            "quality_ratings": {"max_value": 10.00, "min_value": 0.0},
            "vendor": {"error_messages": {"required": _(" vendor Id")}},
        }

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if instance.status == OrderStatus.COMPLETED:
            signals.purchase_order_status_completed.send(
                sender=instance.__class__, instance=instance
            )
        return instance


class AcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ["acknowledge_date"]
        extra_kwargs = {"acknowledgment_date": {"required": True}}

    def validate_acknowledge_date(self, value):
        if not value:
            value = timezone.now()
        return value

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        signals.purchase_order_acknowledged.send(
            sender=instance.__class__, instance=instance
        )
        return instance
