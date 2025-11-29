from rest_framework import serializers
from .models import Book, Author

//this is the AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

// this is the BookSerializer with nested AuthorSerializer and validation for publication_year
class BookSerializer(serializers.ModelSerializer):
    name = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'name']
    
    def validate_publication_year(self, value):
        if value < 0 or value > 2024:
            raise serializers.ValidationError("Publication year must be between 0 and 2024.")
        return value