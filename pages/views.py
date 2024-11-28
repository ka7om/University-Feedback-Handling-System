from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def logIn(request):
    return render(request, "login_app/login_page.html")

def myFeedback(request):
    return render(request, "pages/my_feedback.html")

def feedback(request):
    return render(request, "pages/feedback.html")
