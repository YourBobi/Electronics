from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    country_code = CountryField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}) {self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "Addresses"


class Mail(models.Model):
    mail = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.mail}"

    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"
        db_table = "Mails"


class Contacts(models.Model):
    mail_id = models.ForeignKey(
        "Mail", on_delete=models.PROTECT, verbose_name="Mail ID"
    )
    address_id = models.ForeignKey(
        "Address", on_delete=models.PROTECT, verbose_name="Address ID"
    )

    def __str__(self):
        return f'<"address": "{self.address_id }", "mail": "{self.mail_id.mail}">'

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contacts"
        db_table = "Contacts"


class Staff(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.id}) {self.name}, {self.surname}"

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        db_table = "Staff"
