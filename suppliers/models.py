from django.db import models


class Supplier(models.Model):
    CATEGORY_CHOICES = [
        ("0", "Factory"),
        ("1", "Retail network"),
        ("2", "Individual entrepreneur"),
    ]
    name = models.CharField(verbose_name="Наименование организации", max_length=255)
    email = models.EmailField(verbose_name="Электронная почта", max_length=50)
    country = models.CharField(verbose_name="Страна", max_length=100)
    city = models.CharField(verbose_name="Город", max_length=100)
    street = models.CharField(verbose_name="Улица", max_length=100)
    house_number = models.CharField(verbose_name="Номер дома", max_length=10)
    debt_to_supplier = models.DecimalField(verbose_name="Остаток задолжности", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    supplier_level = models.CharField(verbose_name="Уровень постащика", choices=CATEGORY_CHOICES, max_length=2)
    supplier = models.ForeignKey("self", on_delete=models.CASCADE, related_name="supplier_name", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
        db_table = "suppliers"
