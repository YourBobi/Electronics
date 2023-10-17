from django.core.management.base import BaseCommand
from contacts.models import Address


class Command(BaseCommand):
    help = "Filling in the Address table"

    def handle(self, *args, **kwargs):
        Address()._fill__test_objects(count=100, locale="en")
        self.stdout.write("Filling completed")
