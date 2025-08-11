from rest_framework import serializers
from .models import Author, Book
from datetime import date

# ----------------------------------------------------------
# BookSerializer
# Purpose:
# - Serializes all fields of the Book model.
# - Includes validation to ensure publication_year is not in the future.
# ----------------------------------------------------------
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '_all_'  # Serialize all fields in the Book model

    # Custom field-level validation
    def validate_publication_year(self, value):
        """Ensure the publication year is not in the future."""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# ----------------------------------------------------------
# AuthorSerializer
# Purpose:
# - Serializes the Author model including the 'name' field.
# - Adds a nested BookSerializer to serialize related books dynamically.
# Relationship Handling:
# - Uses 'books' related_name from the ForeignKey in Book to Author.
# ----------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']