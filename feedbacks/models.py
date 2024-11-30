from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link feedback to a user
    topic = models.CharField(max_length=100)  # Topic of feedback
    message = models.TextField()  # Feedback message
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation date


    
    def __str__(self):
        return f"{self.user.username} - {self.topic}"
    
    def upvote_count(self):
        return self.votes.filter(vote_type=Vote.UPVOTE).count()

    def downvote_count(self):
        return self.votes.filter(vote_type=Vote.DOWNVOTE).count()
    
    def score(self):
        return self.upvote_count() - self.downvote_count()
    
class Vote(models.Model):
    UPVOTE = 'U'
    DOWNVOTE = 'D'

    VOTE_CHOICES = [
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')  # User who voted
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='votes')  # Feedback being voted on
    vote_type = models.CharField(max_length=1, choices=VOTE_CHOICES)  # Upvote or Downvote
    created_at = models.DateTimeField(auto_now_add=True)  # When the vote was cast

    class Meta:
        unique_together = ('user', 'feedback')  # Ensure a user can vote only once per feedback

    def __str__(self):
        return f"{self.user.username} - {self.get_vote_type_display()} on {self.feedback.topic}"
