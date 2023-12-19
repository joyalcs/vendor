from django.dispatch import Signal, receiver
from vendor.models import HistoricalPerformance

vendor_history_model = HistoricalPerformance
purchase_order_status_completed = Signal()
purchase_order_acknowledged = Signal()

@receiver(signal=purchase_order_status_completed)
def calc_performance(sender, instance, **kwargs):
    vendor=instance.vendor
    on_time_delivery_rate = vendor.calc_on_time_delivery_rate(),
    quality_rating_average = vendor.calc_quality_rating_average(),
    average_response_time = vendor.calc_average_response_time(),
    fulfillment_rate = vendor.calc_fulfillment_rate(),

    on_time_delivery_rate = on_time_delivery_rate[0] if isinstance(on_time_delivery_rate, tuple) else on_time_delivery_rate
    quality_rating_average = quality_rating_average[0] if isinstance(quality_rating_average, tuple) else quality_rating_average
    average_response_time = average_response_time[0] if isinstance(average_response_time, tuple) else average_response_time
    fulfillment_rate = fulfillment_rate[0] if isinstance(fulfillment_rate, tuple) else fulfillment_rate


    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.quality_rating_average = quality_rating_average
    vendor.average_response_time = average_response_time
    vendor.fulfillment_rate = fulfillment_rate
    vendor.save()
    vendor.refresh_from_db()

    vendor_history_model.objects.create(
        vendor = vendor,
        on_time_delivery_rate =on_time_delivery_rate,
        quality_rating_average=quality_rating_average,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=fulfillment_rate
    )

@receiver(signal=purchase_order_acknowledged)
def calc_avg_response_time(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.average_response_time = vendor.calc_average_response_time()
    vendor.save()
    return vendor
