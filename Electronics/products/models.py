from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    product_model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}) {self.name} - {self.product_model}"

    @staticmethod
    def _fill__test_objects(count=100, locale="en"):
        from mimesis import Generic

        generic = Generic(locale=locale)
        for _ in range(count):
            product = Product(
                name=generic.hardware.manufacturer(),
                date=generic.datetime.date(),
                product_model=generic.hardware.phone_model(),
            )
            product.save()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "Products"
