from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(PerformanceRecord)
