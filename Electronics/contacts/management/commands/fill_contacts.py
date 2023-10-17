from django.core.management.base import BaseCommand
from contacts.models import Contacts


class Command(BaseCommand):
    help = "Filling in the Contacts table"

    def handle(self, *args, **kwargs):
        Contacts()._fill__test_objects(count=100, locale="en")
        self.stdout.write("Filling completed")
