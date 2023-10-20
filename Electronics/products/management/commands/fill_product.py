from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Filling in the Product table"

    def handle(self, *args, **kwargs):
        Product()._fill__test_objects(count=100, locale="en")
        self.stdout.write("Filling completed")
