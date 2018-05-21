from django.urls import path

from api.views import ListBooksView, BooksDetailView, CreateBookView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books-all"),
    path('books/<int:pk>/edit', BooksDetailView.as_view(), name="book-update"),
    path('books/add', CreateBookView.as_view(), name="book-create")
]
