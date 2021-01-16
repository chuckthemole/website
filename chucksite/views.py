from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
#from .models import
from django.contrib.auth.models import User
#from chucksite.models import Script
import os
import subprocess
from django.conf import settings

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
    if request.method == "GET":
        return render(request, "chucksite/projects.html", {})
    else:
        return HttpResponse(status=500)


#Not using now
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def klotski(request):
    os.popen('sh chucksite/static/chucksite/projects/klotski.sh')
    #subprocess.call(['java', '-jar', 'chucksite/static/chucksite/projects/klotski.JAR'])
    
    #os.system("java -jar " + klotski)
    if request.method == "GET":
        return render(request, "chucksite/projects.html", {})
    else:
        return HttpResponse(status=500)
