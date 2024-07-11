from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
     return render(request, "acc/index.html")      

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!") 


def greet(request, name):
    return render(request, "acc/greet.html", {
        "name": name.capitalize()
    })