# Generated by Django 5.2 on 2025-04-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0003_alter_supplier_supplier_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="supplier_level",
            field=models.CharField(
                choices=[("0", "Factory"), ("1", "Retail network"), ("2", "Individual entrepreneur")],
                max_length=2,
                verbose_name="Уровень постащика",
            ),
        ),
    ]
