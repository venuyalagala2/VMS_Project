from rest_framework import serializers
from .models import Vendor, PurchaseOrder, PerformanceRecord


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = "__all__"

    on_time_delivery_rate = serializers.SerializerMethodField()
    quality_rating_average = serializers.SerializerMethodField()
    average_response_time = serializers.SerializerMethodField()
    fulfillment_rate = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseOrder
        fields = "__all__"

    def get_on_time_delivery_rate(self, obj):
        return obj.calculate_on_time_delivery_rate()

    def get_quality_rating_average(self, obj):
        return obj.calculate_quality_rating_average()

    def get_average_response_time(self, obj):
        return obj.calculate_average_response_time()

    def get_fulfillment_rate(self, obj):
        return obj.calculate_fulfillment_rate()


class PerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.SerializerMethodField()
    quality_rating_average = serializers.SerializerMethodField()
    average_response_time = serializers.SerializerMethodField()
    fulfillment_rate = serializers.SerializerMethodField()
