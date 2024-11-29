from django.contrib import admin
from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('home', views.home, name='home'),
    path("my-feedback", views.myFeedback, name="my-feedback"),
    path("feedback", views.feedback, name="feedback"),
    path("browes-feedbacks",views.browes, name ="browes_feedbacks"),
]