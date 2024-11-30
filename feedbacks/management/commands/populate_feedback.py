import random
from django.core.management.base import BaseCommand
from faker import Faker
from feedbacks.models import Feedback, Vote
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate the database with fake feedbacks and votes'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Step 1: Ensure there are users
        if User.objects.count() == 0:
            self.stdout.write("Creating fake users...")
            for _ in range(10):  # Create 10 users
                User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    password="password123"
                )

        users = list(User.objects.all())

        # Step 2: Create fake feedbacks
        self.stdout.write("Creating fake feedbacks...")
        feedbacks = []
        for _ in range(50):  # Create 50 feedbacks
            feedback = Feedback(
                user=random.choice(users),
                topic=fake.sentence(nb_words=6),  # Fake topic
                message=fake.paragraph(nb_sentences=5),  # Fake message
            )
            feedback.save()
            feedbacks.append(feedback)

        # Step 3: Add votes to feedback
        self.stdout.write("Adding votes to feedback...")
        for feedback in feedbacks:
            for _ in range(random.randint(1, len(users))):  # Random votes
                user = random.choice(users)
                vote_type = random.choice(['U', 'D'])  # Upvote or Downvote
                try:
                    Vote.objects.create(
                        user=user,
                        feedback=feedback,
                        vote_type=vote_type
                    )
                except:
                    # Skip if user already voted for this feedback
                    continue

        self.stdout.write(self.style.SUCCESS("Database successfully populated!"))
