from django.contrib.admin import SimpleListFilter
from contacts.models import Address


class ContactsCityFilter(SimpleListFilter):
    """
    City filter
    """

    title = "City"
    parameter_name = "name"

    def lookups(self, request, model_admin):
        """Определение фильтра.

        В качестве параметра выводятся все существующие города.

        Returns
        -------
        city_set: set
            Множество городов.
        """
        city_set = set(
            (address_object.city, address_object.city)
            for address_object in Address.objects.all()
        )
        return city_set

    def queryset(self, request, queryset):
        """Фильтр для queryset.

        Сравниваем есть ли у объекта выбранный город.

        Parameters
        ----------
        queryset : Company()
            queryset класса Company()

        Returns
        -------
        queryset:
            queryset
        """
        if not self.value():
            return queryset
        else:
            return queryset.filter(
                pk__in=[
                    el.id
                    for el in queryset
                    if el.contact_id and el.contact_id.address_id.city == self.value()
                ]
            )
