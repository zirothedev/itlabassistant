from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path("", views.base, name="base"),
    path("signup", views.signup, name="signup"),
    path("login", login_view, name="login"),
    path("home", views.home, name="home")
]