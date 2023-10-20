from django.core.management.base import BaseCommand
from mimesis import Generic
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Filling in the Company table"

    def handle(self, *args, **kwargs):
        generic = Generic(locale="en")
        for _ in range(10):
            user = User.objects.create_user(
                username=generic.person.first_name(),
                email=generic.person.email(),
                password=generic.person.password(),
            )
            user.save()
        self.stdout.write("Filling completed")
