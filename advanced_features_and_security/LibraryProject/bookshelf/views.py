from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from .forms import BookForm
from .forms import ExampleForm

# Create your views here.
# Function-based view for listing books (checker expects book_list)
def book_list(request):
    books = Book.objects.all()  # context variable must be 'books'
    return render(request, "relationship_app/list_books.html", {"books": books})


# Add book (requires can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")  # updated to match view name
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(
        Q(title__icontains=query) | Q(author__name__icontains=query)
    )
    return render(request, "bookshelf/book_list.html", {"books": books})

# Edit book (requires can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form})


# Delete book (requires can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "relationship_app/delete_book.html", {"book": book})

