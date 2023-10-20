from django.core.management.base import BaseCommand
from contacts.models import Mail


class Command(BaseCommand):
    help = "Filling in the Mail table"

    def handle(self, *args, **kwargs):
        Mail()._fill__test_objects(count=100, locale="en")
        self.stdout.write("Filling completed")
