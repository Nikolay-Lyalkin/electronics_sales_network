from django.db import models

from suppliers.models import Supplier


class Product(models.Model):
    name = models.CharField(verbose_name="Наименование продукта", max_length=255)
    model = models.CharField(verbose_name="Наименование модели", max_length=255)
    release_date = models.DateField(verbose_name="Дата выхода продукта на рынок")
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        db_table = "products"
