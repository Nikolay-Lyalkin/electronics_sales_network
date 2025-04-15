from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls", namespace="users")),
    path("", include("products.urls", namespace="products")),
    path("", include("suppliers.urls", namespace="suppliers")),
]
