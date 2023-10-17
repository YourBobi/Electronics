from django.db import models


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
