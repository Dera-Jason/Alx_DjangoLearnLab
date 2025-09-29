from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

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

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)