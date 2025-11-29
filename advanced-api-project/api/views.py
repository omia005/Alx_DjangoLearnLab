from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

