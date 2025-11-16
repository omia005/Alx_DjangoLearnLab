
from django.shortcuts import render, redirect
from .models import Library, Book, Author, Librarian
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, logout, authenticate
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

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm()
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("login")

    return render(request, "register.html")

class LoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True

@login_required
class LogoutView(TemplateView):
    template_name = "logout.html"

    def get(self, request, *args, **kwargs):
        logout(request)  # log the user out
        return super().get(request, *args, **kwargs)



