from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from products.models import Product
from suppliers.models import Supplier


class SupplierSerializer(ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = "__all__"

    def get_products(self, instance):
        products = Product.objects.filter(supplier=instance)
        return products


class SupplierUpdateSerializer(ModelSerializer):

    class Meta:
        model = Supplier
        exclude = ["debt_to_supplier"]
