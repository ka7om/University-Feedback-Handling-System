from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from feedbacks.models import Feedback, Vote

# Create your views here.
def home(request):
    
    return render(request, "pages/home.html")

@login_required
def myFeedback(request):
    return render(request, "pages/my_feedback.html")
@login_required
def feedback(request):
    return render(request, "pages/feedback.html")

def browes(request):
    feedback_list = Feedback.objects.all()  # Optional: To display existing feedbacks
    
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
