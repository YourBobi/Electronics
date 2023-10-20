from django.contrib import admin

from .custom_filters import ContactsCityFilter
from .models import Company

from django.urls import reverse
from django.utils.html import format_html
from .tasks import clear_debt


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
        "copy_email",
    ]
    list_filter = (ContactsCityFilter,)
    actions = ["clear_arrears"]

    def view_provider_links(self, obj):
        """Отображение ссылки на поставщика.

        Parameters
        ----------
        obj : Company()
            Объект класса Company()

        Returns
        -------
        format_html:
            HTML string
        """
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
        """Отображение города компании.

        Parameters
        ----------
        obj : Company()
            Объект класса Company()

        Returns
        -------
        city: str
            Название города
        """
        if obj.contact_id:
            return obj.contact_id.address_id.city

    @admin.action(description="Clear arrears")
    def clear_arrears(self, request, queryset):
        """Очищение задолженности.

        Экшен отчищает задолженность у выбранных компаний. Если выбрано
        больше 20 компаний, очищение происходит асинхронно.

        Parameters
        ----------
        queryset : Company()
            queryset класса Company()
        """
        if len(queryset) > 20:
            for company in queryset:
                clear_debt.delay(company.id)
        else:
            queryset.update(arrears=0)

    def save_model(self, request, obj, form, change):
        """Сохранение модели.

        Переопределение сохранения модели для создания объекта и
        записи поля owner.
        """
        super().save_model(request, obj, form, change)
        obj.save_user(request.user)

    def copy_email(self, obj):
        """Копировать email.

        Копирование происходит в буфер обмена с помощью прописанной js команды
        в onclick.

        Parameters
        ----------
        obj : Company()
            объект класса Company()

        Returns
        -------
        format_html:
            HTML string
        """
        return format_html(
            "<a class=\"button\" onclick=\"navigator.clipboard.writeText('{0}');alert('Скопировано');\">{0}</a>",
            obj.contact_id.mail_id,
        )

    view_provider_links.short_description = "Providers"
    view_company_city.short_description = "Cities"
