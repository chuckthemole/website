from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
#from .models import
from django.contrib.auth.models import User
#from chucksite.models import Script

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "chucksite/index.html", {})
    else:
        return HttpResponse(status=500)

def about(request):
    if request.method == "GET":
        return render(request, "chucksite/about.html", {})
    else:
        return HttpResponse(status=500)

def resume(request):
    if request.method == "GET":
        return render(request, "chucksite/resume.html", {})
    else:
        return HttpResponse(status=500)

def projects(request):
    pass
