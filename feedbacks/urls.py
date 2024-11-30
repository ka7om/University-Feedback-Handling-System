from django.urls import path
from . import views
app_name = 'feedbacks'
urlpatterns = [
    path('submit-feedback', views.submit_feedback, name='submit_feedback'),
    path('feedback/<int:feedback_id>/vote/<str:vote_type>/', views.vote, name='vote'),
]
