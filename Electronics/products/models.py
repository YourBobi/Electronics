from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    product_model = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}) {self.name} - {self.product_model}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "Products"
