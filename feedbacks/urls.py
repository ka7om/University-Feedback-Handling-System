from django.urls import path
from . import views
app_name = 'feedbacks'
urlpatterns = [
    path('submit-feedback', views.submit_feedback, name='submit_feedback'),
]
