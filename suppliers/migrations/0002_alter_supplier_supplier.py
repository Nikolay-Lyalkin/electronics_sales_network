# Generated by Django 5.2 on 2025-04-13 16:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supplier_name",
                to="suppliers.supplier",
            ),
        ),
    ]
