from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor, PurchaseOrder, PerformanceRecord
from .serializers import (
    VendorSerializer,
    PurchaseOrderSerializer,
    PerformanceSerializer,
    PerformanceSerializer,
)


class VendorCreateAPIView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorListAPIView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = "vendor_id"

    def retrieve(self, request, *args, **kwargs):
        vendor_id = kwargs.get("vendor_id")
        try:
            vendor = self.get_queryset().get(id=vendor_id)
            serializer = self.get_serializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            raise NotFound(f"Vendor with id {vendor_id} does not exist.")


class VendorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = "vendor_id"

    def update(self, request, *args, **kwargs):
        vendor_id = kwargs.get("vendor_id")
        try:
            vendor = self.get_queryset().get(id=vendor_id)
            serializer = self.get_serializer(vendor, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            raise NotFound(f"Vendor with id {vendor_id} does not exist.")


class VendorDeleteAPIView(generics.DestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = "vendor_id"

    def destroy(self, request, *args, **kwargs):
        vendor_id = kwargs.get("vendor_id")
        try:
            vendor = self.get_queryset().get(id=vendor_id)
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            raise NotFound(f"Vendor with id {vendor_id} does not exist.")


class PurchaseOrderCreateAPIView(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderListAPIView(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_id = self.request.query_params.get("vendor_id")
        if vendor_id:
            queryset = queryset.filter(vendor=vendor_id)
        return queryset


class PurchaseOrderRetrieveAPIView(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = "po_id"

    def retrieve(self, request, *args, **kwargs):
        po_id = kwargs.get("po_id")
        try:
            purchase_order = self.get_queryset().get(id=po_id)
            serializer = self.get_serializer(purchase_order)
            return Response(serializer.data)
        except PurchaseOrder.DoesNotExist:
            raise NotFound(f"Purchase order with id {po_id} does not exist.")


class PurchaseOrderUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = "po_id"

    def update(self, request, *args, **kwargs):
        po_id = kwargs.get("po_id")
        try:
            purchase_order = self.get_queryset().get(id=po_id)
            serializer = self.get_serializer(purchase_order, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except PurchaseOrder.DoesNotExist:
            raise NotFound(f"Purchase order with id {po_id} does not exist.")


class PurchaseOrderDeleteAPIView(generics.DestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_url_kwarg = "po_id"

    def destroy(self, request, *args, **kwargs):
        po_id = kwargs.get("po_id")
        try:
            purchase_order = self.get_queryset().get(id=po_id)
            purchase_order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrder.DoesNotExist:
            raise NotFound(f"Purchase order with id {po_id} does not exist.")


# performance matric view
# developed logic in purchase model it self
class VendorPerformanceMetricsAPIView(generics.ListAPIView):
    pass
