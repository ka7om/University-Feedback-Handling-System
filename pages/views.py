from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feedbacks.models import Feedback, Vote

# Create your views here.
def home(request):
    
    return render(request, "pages/home.html")

@login_required
def myFeedback(request):
    # Get only feedbacks created by the logged-in user
    feedback_list = sorted(
        Feedback.objects.filter(user=request.user),  # Filter feedbacks by user
        key=lambda feedback: feedback.score(),
        reverse=True,  # Sort from highest to lowest
    )

    user_votes = {}
    feedback_states = {}
    if request.user.is_authenticated:
        user_votes = {
            vote.feedback_id: vote.vote_type
            for vote in Vote.objects.filter(user=request.user)
        }

        # Prepare feedback states for user's feedback
        feedback_states = {
            feedback.id: user_votes.get(feedback.id, None)
            for feedback in feedback_list
        }

    return render(request, "pages/my_feedback.html", {
        'feedback_list': feedback_list,  # Only user feedbacks
        'feedback_states': feedback_states,
    })


    
@login_required
def feedback(request):
    return render(request, "pages/feedback.html")

def browes(request):
    feedback_list = sorted(
        Feedback.objects.all(),
        key=lambda feedback: feedback.score(),
        reverse=True,  # Sort from highest to lowest
    )

    user_votes = {}
    if request.user.is_authenticated:
        user_votes = {
            vote.feedback_id: vote.vote_type
            for vote in Vote.objects.filter(user=request.user)
        }

    return render(request, 'pages/browes_feedbacks.html', {
        'feedback_list': feedback_list,
        'user_votes': user_votes,
    })

