from django.shortcuts import render, redirect
from .forms import UserProfileInfoForm, UserForm

# Create your views here.

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