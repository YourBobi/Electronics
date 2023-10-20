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

    @staticmethod
    def _fill__test_objects(count=100, locale="en"):
        """Метод для заполнения бд.

        С помощью библиотеки mimesis БД заполняется случайными данными.

        Parameters
        ----------
        locale : str
            Язык для передаваемых данных
        count : int
            Количество записей в БД
        """
        from mimesis import Generic

        generic = Generic(locale=locale)
        for _ in range(count):
            address = Address(
                country_code=generic.address.country_code(),
                country=generic.address.country(),
                city=generic.address.city(),
                street=generic.address.street_name(),
                house_number=generic.address.street_number(maximum=100),
            )
            address.save()

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "Addresses"


class Mail(models.Model):
    mail = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.mail}"

    @staticmethod
    def _fill__test_objects(count=100, locale="en"):
        """Метод для заполнения бд.

        С помощью библиотеки mimesis БД заполняется случайными данными.

        Parameters
        ----------
        locale : str
            Язык для передаваемых данных
        count : int
            Количество записей в БД
        """
        from mimesis import Generic

        generic = Generic(locale=locale)
        for _ in range(count):
            email = Mail(mail=generic.person.email())
            email.save()

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

    @staticmethod
    def _fill__test_objects(count=100, locale="en"):
        """Метод для заполнения бд.

        Parameters
        ----------
        locale : str
            Язык для передаваемых данных
        count : int
            Количество записей в БД
        """
        import random

        mails = Mail.objects.all()
        addresses = Address.objects.all()
        for _ in range(count):
            contact = Contacts(
                mail_id=random.choice(mails), address_id=random.choice(addresses)
            )
            contact.save()

    class Meta:
        verbose_name = "Contacts"
        verbose_name_plural = "Contacts"
        db_table = "Contacts"
