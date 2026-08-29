from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_POST

from .services import IceCreamService

def index(request: HttpRequest):
    return render(request, "home.html")

def ice_cream(request: HttpRequest):
    return render(request, "ice_cream.html")

def profile(request: HttpRequest):
    service = IceCreamService()
    person = service.get_user_by_token(request.session["user_token"])
    if request.method == "GET":
        return render(request, "profile.html", {
            "person": person
            })

    elif request.method == "POST":
        person.name = request.POST.get("name")
        person.email = request.POST.get("email")
        person.notification_settings = "notification_settings" in request.POST
        person.current_floor = request.POST.get("current_floor")

        person.save()

        return redirect("profile")


def fridge(request: HttpRequest):
    return render(request, "fridge.html")

@require_POST
def login(request: HttpRequest):
    token = request.POST.get("token")
    role = request.POST.get("role")
    request.session["user_token"] = token
    request.session["role"] = role

    service = IceCreamService()
    service.ensure_user_exists(token, role)

    return redirect("/")

@require_POST
def logout(request: HttpRequest):
    request.session["user_token"] = None
    return redirect("/")
