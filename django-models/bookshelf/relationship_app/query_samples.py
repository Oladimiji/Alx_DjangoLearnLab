# django-models/relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshelf.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # --- Create some sample data ---
    print("--- Creating sample data ---")

    # Authors
    author1, created = Author.objects.get_or_create(name="Jane Austen")
    author2, created = Author.objects.get_or_create(name="George Orwell")

    # Books
    book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
    book2, created = Book.objects.get_or_create(title="1984", author=author2)
    book3, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
    book4, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)

    # Libraries
    library1, created = Library.objects.get_or_create(name="City Central Library")
    library2, created = Library.objects.get_or_create(name="Community Reading Hub")

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2)
    library2.books.add(book3, book4)
    library1.books.add(book4) # A book can be in multiple libraries

    # Librarians
    librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
    # librarian2, created =v Librarian.objects.get_or_create(name="Bob Johnson", library=library2)
    # Note: If you run this script multiple times, trying to create a librarian for library2
    # when one already exists will cause an IntegrityError due to OneToOneField.
    # It's better to use get_or_create and ensure uniqueness for OneToOne.
    # For demonstration, we'll just create one if it doesn't exist.
    if not hasattr(library2, 'librarian'): # Check if a librarian already exists for library2
        Librarian.objects.create(name="Bob Johnson", library=library2)
    else:
        print(f"Librarian for {library2.name} already exists.")


    print("\n--- Running Queries ---")

    # Query 1: Query all books by a specific author.
    print("\n--- Books by Jane Austen ---")
    jane_austen = Author.objects.get(name="Jane Austen")
    books_by_jane = jane_austen.books.all() # Using related_name 'books'
    for book in books_by_jane:
        print(f"- {book.title}")

    # Query 2: List all books in a library.
    print("\n--- Books in City Central Library ---")
    city_library = Library.objects.get(name="City Central Library")
    books_in_city_library = city_library.books.all()
    for book in books_in_city_library:
        print(f"- {book.title}")

    # Query 3: Retrieve the librarian for a library.
    print("\n--- Librarian for Community Reading Hub ---")
    community_library = Library.objects.get(name="Community Reading Hub")
    try:
        community_librarian = community_library.librarian # Using related_name 'librarian'
        print(f"- The librarian for {community_library.name} is {community_librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {community_library.name}")

if __name__ == "_main_":
    run_queries()