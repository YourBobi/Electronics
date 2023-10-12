from django_filters import (
    FilterSet,
    AllValuesFilter,
)


class CompanyFilter(FilterSet):
    country = AllValuesFilter(
        field_name="contact_id__address_id__country_code", label="Country"
    )
