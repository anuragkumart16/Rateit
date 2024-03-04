from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from datetime import datetime
from .models import CustomUser
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def home(request):
    return render(request,"index.html")

def sign_in(request):
    return render(request,"login.html")

def loggingin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        print(username,password)
        if user is not None:
            # Login the user
            login(request, user)
            # Redirect the user to the home page
            return redirect('/land/')  # Assuming 'home' is the name of the URL pattern for the home page
        else:
            # Authentication failed
            messages.error(request, 'Invalid username or password.')
            # Redirect back to the login page
            return redirect('signin')  # Assuming 'sign_in' is the name of the URL pattern for the login page

    # If the request method is not POST, simply redirect to the login page
    return redirect('signin')  # Assuming 'sign_in' is the name of the URL pattern for the login page

def sign_up(request):
    return render(request,'signup.html')



def register(request):
    if request.method == 'POST':
        # Extract user data from the POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        
        # Extract date, month, and year from the POST request
        day = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')
        
        # Merge date, month, and year into a single string in format 'YYYY-MM-DD'
        date_of_birth_str = f'{year}-{month}-{day}'
        
        # Convert the string into a datetime object
        date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d').date()
        contact_number = request.POST.get('contact')
        
        # # checking if user already exists
        # if CustomUser.objects.filter(username=username).exists():
        #     error_message = "Username is already taken. Please choose a different username."
        #     return redirect(reverse('signup') + f'?error_message={error_message}')
        
        # Create a new CustomUser object and save it to the database
        user = CustomUser(
            username=username,
            email=email,
            password=make_password(password),  # Hash the password
            # password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            contact_number=contact_number
        )
        user.save()
        
        # Redirect to a success page or any other page as needed
        messages.success(request, 'User created successfully. You can now log in.')
        return redirect('/login/')
        
    else:
        return render(request, 'signup.html')


def logout_view(request):
    logout(request)
    # Redirect to a desired page after logging out
    return redirect('signin')  # Replace 'home' with the name of the URL pattern you want to redirect to


def check_username_availability(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username:
            if CustomUser.objects.filter(username=username).exists():
                return JsonResponse({'available': False})
            else:
                return JsonResponse({'available': True})
    return JsonResponse({'error': 'Invalid request'})


