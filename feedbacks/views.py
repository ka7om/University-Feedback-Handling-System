from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback
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

