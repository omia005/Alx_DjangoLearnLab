
from django.shortcuts import render, redirect
from .models import Library, Book, Author, Librarian
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#view for listing all boks in the Library
def list_books(request):
  books = Book.objects.all()
  context = {"Books":books}
  
  return render(request, "relationship_app/list_books.html", context)

#view for providing library details
class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'
  context_object_name = "library"
  
  def get_context_data():
    context= super().get_context_data( **kwargs)
    context["books"] = self.object.books.all()
    return context

class RegistrationView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relashionship_app/register.html'

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "relationship_app/login.html")

@login_required
class LogoutPageView(TemplateView):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        logout(request)  # log the user out
        return super().get(request, *args, **kwargs)



