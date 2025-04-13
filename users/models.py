from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(unique=True, verbose_name="Никнейм пользователя",  max_length=30)
    email = models.EmailField(unique=True, verbose_name="Электронная почта", max_length=50)
    name_company = models.CharField(verbose_name="Наименование компании", blank=True, null=True, max_length=50)
    phone_number = models.CharField(verbose_name="Номер телефона", blank=True, null=True, max_length=20)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "users"

    def __str__(self):
        return f"{self.email}"
