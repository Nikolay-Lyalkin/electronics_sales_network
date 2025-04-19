from django.urls import path

from . import views
from .apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    # habits
    path("products/", views.ProductListAPIView.as_view(), name="product_list"),
    path("product/create/", views.ProductCreateAPIView.as_view(), name="product_create"),
    path("product/<int:pk>/update/", views.ProductUpdateAPIView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", views.ProductDeleteAPIView.as_view(), name="product_delete"),
    path("product/<int:pk>/", views.ProductRetrieveAPIView.as_view(), name="product_retrieve"),
]
