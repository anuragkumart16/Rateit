from django.shortcuts import render,redirect
from .forms import UserRegistrationForm

# Create your views here.

def home(request):
    return render(request,"index.html")

def sign_in(request):
    return render(request,"login.html")

def sign_up(request):
    return render(request,'signup.html')


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
        print("else is being executed")
    return render(request, 'signup.html', {'form': form})

def registration_success(request):
    return render(request, 'login.html')
