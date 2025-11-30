from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['publication_year', 'author', 'title']
    search_fields = ['title', 'author']
    ordering_fields = ['publication_year', 'title']
    ordering = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users


class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create
    
    def perform_create(self, serializer):
        """Customize the creation process"""
        # Add the current user as the book owner/creator
        serializer.save(created_by=self.request.user)
        
    def create(self, request, *args, **kwargs):
        """Override create to add custom validation and response"""
        try:
            # Custom pre-validation logic
            if not self.is_valid_submission(request):
                return Response(
                    {"error": "Invalid submission data"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            response = super().create(request, *args, **kwargs)
            
            # Customize the response
            response.data['message'] = 'Book created successfully'
            response.data['book_id'] = response.data['id']
            return response
            
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def is_valid_submission(self, request):
        """Custom validation method"""
        # Example: Check if user can create more books
        user_books_count = Book.objects.filter(created_by=request.user).count()
        if user_books_count >= 10:  # Limit users to 10 books
            return False
        return True

         
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthenticatedOrReadOnly]  # Only owner can update
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        """Customize the update process"""
        # Add update timestamp or track who modified
        serializer.save(updated_by=self.request.user)
        
    def update(self, request, *args, **kwargs):
        """Override update to add custom validation and response"""
        try:
            # Get the object first to check permissions
            instance = self.get_object()
            
            # Custom validation before update
            if not self.can_update(instance, request):
                return Response(
                    {"error": "Update not allowed"}, 
                    status=status.HTTP_403_FORBIDDEN
                )
                
            response = super().update(request, *args, **kwargs)
            
            # Customize the response
            response.data['message'] = 'Book updated successfully'
            return response
            
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def can_update(self, instance, request):
        """Custom method to check if update is allowed"""
        # Example: Prevent updates if book is published
        if instance.status == 'published':
            return False
        return True


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

