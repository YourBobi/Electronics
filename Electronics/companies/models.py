from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    COMPANY_TYPE = [
        ("FY", "Factory"),
        ("DI", "Distributor"),
        ("DE", "Dealership"),
        ("LRC", "Large retail chain"),
        ("IE", "Individual entrepreneur"),
    ]
    owner = models.ForeignKey(User, related_name="companies", on_delete=models.CASCADE)
    level = models.IntegerField()
    type = models.CharField(choices=COMPANY_TYPE, max_length=50)
    name = models.CharField(max_length=50)
    arrears = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", blank=True, null=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    product_id = models.ManyToManyField(
        "products.Product", verbose_name="Products ID", blank=True
    )
    staff_id = models.ManyToManyField(
        "companies_details.Staff", verbose_name="Staff", blank=True
    )
    provider_id = models.ForeignKey(
        "self", on_delete=models.PROTECT, blank=True, null=True
    )
    contact_id = models.OneToOneField(
        "companies_details.Contacts", on_delete=models.CASCADE
    )

    def __str__(self):
        return f'<"id": "{self.id}", "name":"{self.name}">'

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        db_table = "Companies"
