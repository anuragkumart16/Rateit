from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,"index.html")

def sign_in(request):
    return render(request,"login.html")

def sign_up(request):
    return render(request,'signup.html')