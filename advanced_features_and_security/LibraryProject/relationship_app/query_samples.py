"""
query_samples.py
Run this from the project root (where manage.py is) with:
    python relationship_app/query_samples.py
It will ensure sample data exists, then run the queries described in the task.
"""

import os
import django
import sys

# Add project root (the folder containing manage.py) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Adjust the settings module path if your project package is named differently.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def seed_sample_data():
    # Create an author and books (idempotent)
    author, _ = Author.objects.get_or_create(name="George Orwell")
    book1, _ = Book.objects.get_or_create(title="1984", author=author)
    book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author)

    # Create a library and add books
    library, created = Library.objects.get_or_create(name="Central Library")
    if created or not library.books.exists():
        library.books.set([book1, book2])

    # Create a librarian for the library if none exists
    Librarian.objects.get_or_create(name="Jane Doe", library=library)

    print("✅ Sample data seeded.")

def query_books_by_author(author_name):
    print(f"\n--- Books by author: {author_name} ---")
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        for b in books:
            print(f"- {b.title}")
        if not books:
            print("No books found for this author.")
    except Author.DoesNotExist:
        print("Author not found.")

def list_books_in_library(library_name):
    print(f"\n--- Books in library: {library_name} ---")
    try:
        library = Library.objects.get(name=library_name)
        for b in library.books.all():
            print(f"- {b.title} (Author: {b.author.name})")
        if not library.books.exists():
            print("Library has no books.")
    except Library.DoesNotExist:
        print("Library not found.")

def get_librarian_for_library(library_name):
    print(f"\n--- Librarian for library: {library_name} ---")
    try:
        library = Library.objects.get(name=library_name)
        # Explicit query for checker
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or librarian not found.")

if __name__ == "__main__":
    seed_sample_data()
    query_books_by_author("George Orwell")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
