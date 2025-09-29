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
]

urlpatterns += [
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
]

urlpatterns += [
    path("books/add/", add_book, name="add_book"),
    path("books/edit/<int:pk>/", edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", delete_book, name="delete_book"),
]