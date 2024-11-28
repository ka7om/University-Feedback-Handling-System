from django.shortcuts import render, redirect
from .forms import UserProfileInfoForm, UserForm
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def logIn(request):
    return render(request, "login_app/login_page.html")

def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST, request.FILES)
    
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            return redirect('pages:home')
        else:
            print(user_form.errors, profile_form.errors)  # This will help identify the validation errors
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, "login_app/registartion.html", {"user_form":user_form,"profile_form":profile_form,"registered":registered})

@login_required
def user_logout(request):
    logout(request)
    return render(request, "pages/home.html",{})

def logIn(request):
    return render(request, "login_app/login_page.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('pages:home'))
            else:
                return HttpResponse("Account is not active")
        else:
            return render(request, "login_app/login_page.html", {"error_message": "Invalid username or password"})
    return render(request, "login_app/login_page.html")
