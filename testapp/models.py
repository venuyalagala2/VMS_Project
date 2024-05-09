from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("canceled", "Canceled"),
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def calculate_on_time_delivery_rate(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor, status="completed"
        )
        on_time_deliveries = completed_pos.filter(
            delivery_date__lte=timezone.now()
        ).count()
        total_completed_pos = completed_pos.count()
        if total_completed_pos > 0:
            return on_time_deliveries / total_completed_pos
        return 0

    def calculate_quality_rating_average(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor, status="completed"
        ).exclude(quality_rating__isnull=True)
        total_ratings = completed_pos.aggregate(total=models.Sum("quality_rating"))[
            "total"
        ]
        count = completed_pos.count()
        if count > 0:
            return total_ratings / count
        return 0

    def calculate_average_response_time(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor, status="completed"
        ).exclude(acknowledgment_date__isnull=True)
        total_response_time = sum(
            (po.acknowledgment_date - po.issue_date).total_seconds()
            for po in completed_pos
        )
        count = completed_pos.count()
        if count > 0:
            return total_response_time / count
        return 0

    def calculate_fulfillment_rate(self):
        completed_pos = PurchaseOrder.objects.filter(
            vendor=self.vendor, status="completed"
        )
        fulfilled_pos = completed_pos.filter(
            status="completed", quality_rating__isnull=False
        )
        total_pos = completed_pos.count()
        if total_pos > 0:
            return fulfilled_pos.count() / total_pos
        return 0


class PerformanceRecord(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
