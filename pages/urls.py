from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path("login", views.logIn, name="login"),
    path("my-feedback", views.myFeedback, name="my-feedback"),
    path("feedback", views.feedback, name="feedback")
]