from django.urls import path, include
from . import views
app_name = "login"
urlpatterns = [
    path('registration', views.register, name="register"),
    path('login', views.logIn, name="login_page"),
    path('login/auth', views.user_login, name="user_login"),
]