from django.contrib import admin
from .models import Company

from django.urls import reverse
from django.utils.html import format_html


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "level",
        "name",
        "type",
        "arrears",
        "creation_date",
        "view_provider_links",
    ]

    def view_provider_links(self, obj):
        if obj.provider_id:
            url = reverse(
                "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name),
                args=(obj.provider_id.id,),
            )
            return format_html(
                '<a href="{}">{} [company_id:{}]</a>',
                url,
                obj.provider_id.name,
                obj.provider_id.id,
            )
