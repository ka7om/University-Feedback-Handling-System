from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Generate fake users"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Number of users to create
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='defaultpassword123'  # Default password for all users
            )
        self.stdout.write(self.style.SUCCESS("10 fake users created!"))
