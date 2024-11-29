from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    
    return render(request, "pages/home.html")

@login_required
def myFeedback(request):
    return render(request, "pages/my_feedback.html")
@login_required
def feedback(request):
    return render(request, "pages/feedback.html")
