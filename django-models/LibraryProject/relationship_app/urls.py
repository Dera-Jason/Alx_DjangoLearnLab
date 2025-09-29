from django.urls import path
from . import views  # import views for register
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView  # your book/library views
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    # Book and library views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication
    path("register/", views.register, name="register"),  # must be named 'register'
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),

    # Add the missing permission-protected views
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Role-based views
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
]
