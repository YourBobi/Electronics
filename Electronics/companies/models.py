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
    level = models.IntegerField()
    type = models.CharField(choices=COMPANY_TYPE, max_length=50)
    name = models.CharField(max_length=50)
    arrears = MoneyField(
        max_digits=14, decimal_places=2, default_currency="USD", blank=True, default=0
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    owner = models.ManyToManyField(User, related_name="companies", editable=False)
    product_id = models.ManyToManyField(
        "products.Product", verbose_name="Products ID", blank=True
    )
    staff_id = models.ManyToManyField("staff.Staff", verbose_name="Staff", blank=True)
    provider_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True
    )
    contact_id = models.OneToOneField("contacts.Contacts", on_delete=models.CASCADE)

    def save_user(self, user):
        self.owner.add(user)

    def __str__(self):
        return f'<"id": "{self.id}", "name":"{self.name}">'

    @staticmethod
    def _fill__test_objects(locale="en"):
        """Метод для заполнения бд.

        С помощью библиотеки mimesis БД заполняется случайными данными.

        Parameters
        ----------
        locale : str
            Язык для передаваемых данных
        """
        from mimesis import Generic
        import random
        from products.models import Product
        from staff.models import Staff
        from contacts.models import Contacts

        generic = Generic(locale=locale)
        products = Product.objects.all()
        staff = Staff.objects.all()
        types = Company.COMPANY_TYPE
        users = User.objects.all()
        # Исключаю существующие контакты
        contacts = list(
            Contacts.objects.all().exclude(
                id__in=Company.objects.values_list("contact_id", flat=True)
            )
        )
        providers_id = [None]
        for _ in range(len(contacts)):
            # берем непривязанную компанию
            contact = random.choice(contacts)
            contacts.remove(contact)
            #  создание объекта
            product = Company(
                level=generic.numeric.integer_number(start=0, end=5),
                type=random.choice(types)[1],
                name=generic.hardware.manufacturer(),
                arrears=generic.numeric.float_number(start=0.1, end=1000, precision=2),
                provider_id=random.choice(providers_id),
                contact_id=contact,
            )
            # чтобы записать manyToMany нужен id компании
            product.save()
            # запись manyToMany
            product.owner.add(random.choice(users))
            product.product_id.add(random.choice(products))
            product.staff_id.add(random.choice(staff))
            product.save()
            providers_id.append(product)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        db_table = "Companies"
