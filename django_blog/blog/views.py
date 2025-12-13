from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def login_view(request):
    return render(request, 'blog/login.html')

def logout_view(request):
    return render(request, 'blog/logout.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
     form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def profile_view(request):
    return render(request, 'blog/profile.html')
    

def home_view(request):
    return render(request, 'blog/home.html')