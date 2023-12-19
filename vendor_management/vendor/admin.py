from django.contrib import admin
from .models import Vendor, HistoricalPerformance
# Register your models here.
admin.site.register(HistoricalPerformance)
admin.site.register(Vendor)
