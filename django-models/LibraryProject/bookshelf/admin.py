from django.contrib import admin
from .models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters in the right sidebar
    list_filter = ('publication_year', 'author')

    # Add search box for quick searching
    search_fields = ('title', 'author')

    # Optional: allow quick editing of some fields directly in list view
    # list_editable = ('publication_year',)

    # Optional: ordering defaults
    ordering = ('title',)