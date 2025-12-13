from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def register_view(request):
    return render(request, 'register.html')

def profile_view(request):
    return render(request, 'profile.html')

def home_view(request):
    return render(request, 'home.html')