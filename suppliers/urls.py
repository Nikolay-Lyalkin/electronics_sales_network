from django.urls import path

from . import views
from .apps import SuppliersConfig

app_name = SuppliersConfig.name

urlpatterns = [
    # habits
    path("suppliers/", views.SupplierListAPIView.as_view(), name="supplier_list"),
    path("supplier/create/", views.SupplierCreateAPIView.as_view(), name="supplier_create"),
    path("supplier/<int:pk>/update/", views.SupplierUpdateAPIView.as_view(), name="supplier_update"),
    path("supplier/<int:pk>/delete/", views.SupplierDeleteAPIView.as_view(), name="supplier_delete"),
    path("supplier/<int:pk>/", views.SupplierRetrieveAPIView.as_view(), name="supplier_retrieve"),
]
