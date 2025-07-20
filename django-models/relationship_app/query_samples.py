import os
import django
import sys # <--- Add this line

# Get the path to the project root directory (one level up from relationship_app)
# Assuming query_samples.py is in relationship_app, and relationship_app is in the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root) # <--- Add this line to add project root to sys.path

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookshelf.settings') # Keep this as 'bookshelf.settings'
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Creating sample data ---")
    # ... rest of your run_queries function ...

if __name__ == '__main__':
    run_queries()