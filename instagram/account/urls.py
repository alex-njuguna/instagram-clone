from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


app_name = "account"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("signin/", LoginView.as_view(template_name="signin.html", next_page="post:index"), name="signin"),
]