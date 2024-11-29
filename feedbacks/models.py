from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link feedback to a user
    topic = models.CharField(max_length=100)  # Topic of feedback
    message = models.TextField()  # Feedback message
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation date

    def __str__(self):
        return f"{self.user.username} - {self.topic}"
