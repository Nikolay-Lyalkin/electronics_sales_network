from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product
from suppliers.models import Supplier
from users.models import User


class ProductTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", email="test@yandex.ru", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.supplier = Supplier.objects.create(
            name="ООО Груша",
            email="test@yandex.ru",
            country="Москва",
            city="Нижний Новгород",
            street="Полоцкая",
            house_number="20",
            debt_to_supplier=23450.30,
            supplier_level="0",
        )
        self.product = Product.objects.create(
            name="IPhone", model="16ProMax", release_date="2025-07-23", supplier=self.supplier
        )

    def test_product_create(self):
        data = {"name": "IPhone", "model": "16proMax", "release_date": "2025-07-23", "supplier": 1}

        response = self.client.post("/product/create/", data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(
            response.json(), {"name": "IPhone", "model": "16proMax", "release_date": "2025-07-23", "supplier": 1}
        )
        self.assertTrue(Product.objects.all().exists())

    def test_product_list(self):
        response = self.client.get("/products/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(), [{"name": "IPhone", "model": "16ProMax", "release_date": "2025-07-23", "supplier": 1}]
        )

    def test_product_patch(self):

        data = {"model": "16Pro"}

        response = self.client.patch("/product/1/update/", data=data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json(), {"name": "IPhone", "model": "16Pro", "release_date": "2025-07-23", "supplier": 1}
        )

    def test_product_delete(self):

        response = self.client.delete("/product/1/delete/")

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
