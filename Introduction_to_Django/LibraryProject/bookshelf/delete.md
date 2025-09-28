# CREATE Operation

# Command
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(id=1)

# Delete the book
book.delete()

# Confirm deletion
Book.objects.all()


# Expected Output
(1, {'bookshelf.Book': 1})
<QuerySet []>
