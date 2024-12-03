from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Feedback, Vote
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required


@login_required
def submit_feedback(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to submit feedback.")
        return redirect('login:login_page')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Associate feedback with the logged-in user
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('pages:home')
        else:
            messages.error(request, "There was an error in your submission. Please try again.")
    else:
        form = FeedbackForm()

    feedback_list = Feedback.objects.all()  # Optional: To display existing feedbacks
    return render(request, 'feedbacks/feedbacks.html', {'form': form, 'feedback_list': feedback_list})

def vote(request, feedback_id, vote_type):
    """
    Handles upvotes and downvotes for feedback.
    Parameters:
    - feedback_id: ID of the feedback being voted on.
    - vote_type: 'U' for upvote, 'D' for downvote.
    """
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to vote.")
        return redirect('login:login_page')

    feedback = get_object_or_404(Feedback, id=feedback_id)

    # Check if the user has already voted on this feedback
    vote = Vote.objects.filter(user=request.user, feedback=feedback).first()

    if vote:
        # Update existing vote if different
        if vote.vote_type != vote_type:
            vote.vote_type = vote_type
            vote.save()
            messages.success(request, "Your vote has been updated.")
        else:
            # If the same vote exists, remove it (toggle feature)
            vote.delete()
            messages.success(request, "Your vote has been removed.")
    else:
        # Create a new vote
        Vote.objects.create(user=request.user, feedback=feedback, vote_type=vote_type)
        messages.success(request, "Your vote has been recorded.")

    return redirect('pages:browes_feedbacks')  # Redirect to your feedback list page

def vote2(request, feedback_id, vote_type):
    """
    Handles upvotes and downvotes for feedback.
    Parameters:
    - feedback_id: ID of the feedback being voted on.
    - vote_type: 'U' for upvote, 'D' for downvote.
    """
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to vote.")
        return redirect('login:login_page')

    feedback = get_object_or_404(Feedback, id=feedback_id)

    # Check if the user has already voted on this feedback
    vote = Vote.objects.filter(user=request.user, feedback=feedback).first()

    if vote:
        # Update existing vote if different
        if vote.vote_type != vote_type:
            vote.vote_type = vote_type
            vote.save()
            messages.success(request, "Your vote has been updated.")
        else:
            # If the same vote exists, remove it (toggle feature)
            vote.delete()
            messages.success(request, "Your vote has been removed.")
    else:
        # Create a new vote
        Vote.objects.create(user=request.user, feedback=feedback, vote_type=vote_type)
        messages.success(request, "Your vote has been recorded.")

    return redirect('pages:my_feedback')  # Redirect to your feedback list page