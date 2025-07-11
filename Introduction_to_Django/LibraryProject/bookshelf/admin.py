from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    list_filter = ('publication_year', 'author')            # Filters in sidebar
    search_fields = ('title', 'author')                     # Search bar