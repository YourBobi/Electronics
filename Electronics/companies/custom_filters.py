from django.contrib.admin import SimpleListFilter
from companies_details.models import Address


class ContactsCityFilter(SimpleListFilter):
    """
    City filter
    """

    title = "City"
    parameter_name = "name"

    def lookups(self, request, model_admin):
        city_set = set(
            (address_object.city, address_object.city)
            for address_object in Address.objects.all()
        )
        # city_set.add(("-", "-"))
        return city_set

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        # elif self.value() == "-":
        #     return queryset.filter(
        #         pk__in=[el.id for el in queryset if not el.contact_id]
        #     )
        else:
            return queryset.filter(
                pk__in=[
                    el.id
                    for el in queryset
                    if el.contact_id and el.contact_id.address_id.city == self.value()
                ]
            )
