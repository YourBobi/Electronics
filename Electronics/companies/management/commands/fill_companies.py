from django.core.management.base import BaseCommand
from companies.models import Company


class Command(BaseCommand):
    help = "Filling in the Company table"

    def handle(self, *args, **kwargs):
        Company()._fill__test_objects(locale="en")
        self.stdout.write("Filling completed")
