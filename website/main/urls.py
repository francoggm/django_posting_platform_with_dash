from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("sign-up/", views.sign_up, name="sign-up"),
    path("create-post/", views.create_post, name="create-post"),
    path("password_change/", auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change.html"
    ), name="password_change"),
    path("login/", auth_views.LoginView.as_view(
        template_name="registration/login.html"
    ), name="login"),
]