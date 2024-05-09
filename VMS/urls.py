"""
URL configuration for VMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from testapp.views import (
    VendorCreateAPIView,
    VendorListAPIView,
    VendorRetrieveAPIView,
    VendorUpdateAPIView,
    VendorDeleteAPIView,
    PurchaseOrderCreateAPIView,
    PurchaseOrderListAPIView,
    PurchaseOrderRetrieveAPIView,
    PurchaseOrderUpdateAPIView,
    PurchaseOrderDeleteAPIView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/vendors/", VendorCreateAPIView.as_view(), name="vendor-create"),
    path("api/vendors_details/", VendorListAPIView.as_view(), name="vendor-list"),
    path(
        "api/vendors/<int:vendor_id>/",
        VendorRetrieveAPIView.as_view(),
        name="vendor-retrieve",
    ),
    path(
        "api/updatevendor/<int:vendor_id>/",
        VendorUpdateAPIView.as_view(),
        name="vendor-update",
    ),
    path(
        "api/deletevendors/<int:vendor_id>/",
        VendorDeleteAPIView.as_view(),
        name="vendor-delete",
    ),
    # Purchase Orders
    path(
        "api/purchase_orders/",
        PurchaseOrderCreateAPIView.as_view(),
        name="purchase-order-create",
    ),
    path(
        "api/purchase_order/",
        PurchaseOrderListAPIView.as_view(),
        name="purchase-order-list",
    ),
    path(
        "api/purchase_orders/<int:po_id>/",
        PurchaseOrderRetrieveAPIView.as_view(),
        name="purchase-order-retrieve",
    ),
    path(
        "api/purchase_orders_update/<int:po_id>/",
        PurchaseOrderUpdateAPIView.as_view(),
        name="purchase-order-update",
    ),
    path(
        "api/purchase_orders_delete/<int:po_id>/",
        PurchaseOrderDeleteAPIView.as_view(),
        name="purchase-order-delete",
    ),
    # path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceMetricsAPIView.as_view(), name='vendor-performance-metrics'),
    # path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceMetricsRetrieveAPIView.as_view(), name='vendor-performance-metrics'),
]
