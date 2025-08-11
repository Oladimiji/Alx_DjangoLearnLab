from django.db import models

# ----------------------------------------------------------
# Author Model
# Purpose:
# - Represents an author of one or more books.
# - 'name' stores the author's name.
# Relationships:
# - Has a one-to-many relationship with Book via ForeignKey.
# ----------------------------------------------------------
class Author(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name


# ----------------------------------------------------------
# Book Model
# Purpose:
# - Represents a book with title, publication year, and its author.
# - 'author' ForeignKey establishes the link to Author.
# Relationships:
# - Many books can belong to a single author.
# ----------------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def _str_(self):
        return self.title