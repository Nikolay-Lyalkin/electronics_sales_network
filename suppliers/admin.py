from django.contrib import admin
from django.utils.html import format_html

from suppliers.models import Supplier


@admin.action(description="clear debt")
def clear_debt(self, request, queryset):
    for obj in queryset:
        obj.debt_to_supplier = 0  # Обнуление задолженности
        obj.save()
    self.message_user(request, "Задолженность успешно обнулена.")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "debt_to_supplier", "supplier_level", "supplier", "supplier_link", "created_at"]
    list_filter = ("city",)
    actions = [clear_debt]

    def supplier_link(self, obj):
        """Добавить ссылку на поставщика."""
        if obj.supplier:
            return format_html('<a href="/admin/suppliers/supplier/{}/">{}</a>', obj.supplier.id, obj.supplier.name)
        return "-"

    supplier_link.short_description = "Cсылка на поставщика"
