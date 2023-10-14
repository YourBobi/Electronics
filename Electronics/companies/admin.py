from django.contrib import admin

from .custom_filters import ContactsCityFilter
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
        "view_company_city",
    ]
    list_filter = (ContactsCityFilter,)
    actions = ["clear_arrears"]

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

    def view_company_city(self, obj):
        if obj.contact_id:
            return obj.contact_id.address_id.city

    @admin.action(description="Clear arrears")
    def clear_arrears(self, request, queryset):
        queryset.update(arrears=0)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.save_user(request.user)

    view_provider_links.short_description = "Providers"
    view_company_city.short_description = "Cities"
