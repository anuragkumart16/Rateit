from django.shortcuts import render

def profiles(request):
    return render(request, 'profile-index.html')

def land(request):
    return render(request,'land.html')
