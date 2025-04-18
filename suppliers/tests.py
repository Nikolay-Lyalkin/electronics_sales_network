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

    def test_supplier_create(self):
        data = {
            "name": "ООО Груша",
            "email": "test@yandex.ru",
            "country": "Москва",
            "city": "Нижний Новгород",
            "street": "Полоцкая",
            "house_number": 20,
            "debt_to_supplier": 23450.30,
            "supplier_level": "0",
        }

        response = self.client.post("/supplier/create/", data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json().get("name"), "ООО Груша")
        self.assertTrue(Product.objects.all().exists())

    def test_supplier_list(self):

        response = self.client.get("/suppliers/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            response.json()[0].get("products"),
            [{"name": "IPhone", "model": "16ProMax", "release_date": "2025-07-23", "supplier": 1}],
        )

    def test_supplier_patch(self):

        data = {"city": "Москва"}
        data_change_debt = {"debt_to_supplier": 0}

        response = self.client.patch("/supplier/1/update/", data=data)
        response_change_debt = self.client.patch("/supplier/1/update/", data=data_change_debt)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json().get("city"), "Москва")
        self.assertEquals(response_change_debt.json(), {"message": "Поле задолжности изменять нельзя"})

    def test_supplier_delete(self):

        response = self.client.delete("/supplier/1/delete/")

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
