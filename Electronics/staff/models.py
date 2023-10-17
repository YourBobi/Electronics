from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.id}) {self.name}, {self.surname}"

    @staticmethod
    def _fill__test_objects(count=100, locale="en"):
        from mimesis import Generic

        generic = Generic(locale=locale)
        for _ in range(count):
            employ = Staff(
                name=generic.email(),
                phone_number=generic.telephone(),
                surname=generic.surname(),
            )
            employ.save()

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        db_table = "Staff"
