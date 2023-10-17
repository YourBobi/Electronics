from django.core.management.base import BaseCommand
from staff.models import Staff


class Command(BaseCommand):
    help = "Filling in the Staff table"

    def handle(self, *args, **kwargs):
        Staff()._fill__test_objects(count=100, locale="en")
        self.stdout.write("Filling completed")
