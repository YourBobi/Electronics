from django_filters import FilterSet, AllValuesFilter, ChoiceFilter
from statistics import mean


class CompanyFilter(FilterSet):
    # Фильтр по стране
    country = AllValuesFilter(
        field_name="contact_id__address_id__country_code", label="Country"
    )
    # Фильтр вывести компании превышающие среднюю задолженность
    debt = ChoiceFilter(
        choices=(("true", "Company with debt"),),
        label="Company with debt",
        method="filter_company_debt",
        # widget=django_filters.widgets.LinkWidget,
    )
    # Фильтр по id продукта
    id = AllValuesFilter(field_name="product_id", label="Product ID")

    def filter_company_debt(self, queryset, name, value):
        """Метод для средней задолженности.

        Определяется средняя задолженность компаний и возвращаются те компании,
        у которых задолженность выше средней.
        """
        average_debt = mean([company.arrears.amount for company in queryset])
        return queryset.filter(arrears__gte=average_debt)
