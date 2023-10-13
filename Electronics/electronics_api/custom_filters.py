from django_filters import FilterSet, AllValuesFilter, ChoiceFilter
from statistics import mean


class CompanyFilter(FilterSet):
    country = AllValuesFilter(
        field_name="contact_id__address_id__country_code", label="Country"
    )
    debt = ChoiceFilter(
        choices=(("true", "Company with debt"),),
        label="Company with debt",
        method="filter_company_debt",
        # widget=django_filters.widgets.LinkWidget,
    )

    def filter_company_debt(self, queryset, name, value):
        average_debt = mean([company.arrears.amount for company in queryset])
        return queryset.filter(arrears__gte=average_debt)
