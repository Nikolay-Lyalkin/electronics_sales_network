from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer, SupplierUpdateSerializer


class SupplierListAPIView(generics.ListAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "country",
    ]
    ordering_fields = [
        "country",
    ]
    permission_classes = [IsAuthenticated]


class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class SupplierUpdateAPIView(generics.UpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierUpdateSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        if request.data.get("debt_to_supplier"):
            message = "Поле задолжности изменять нельзя"
            return Response({"message": message})
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if request.data.get("debt_to_supplier"):
            message = "Поле задолжности изменять нельзя"
            return Response({"message": message})
        return self.update(request, *args, **kwargs)


class SupplierDeleteAPIView(generics.DestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
