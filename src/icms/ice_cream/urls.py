from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ice-cream/", views.ice_cream, name="ice_cream"),
    path("profile/", views.profile, name="profile"),
    path("fridge/", views.fridge, name="fridge"),
    path("user/login/", views.login, name="login"),
    path("user/logout/", views.logout, name="logout")
]