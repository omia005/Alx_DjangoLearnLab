from django.shortcuts import render
from .models import Library, Book, Author, Librarian
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

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
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relashionship_app/register.html'


