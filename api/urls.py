from django.urls import path

from api.views import ListBooksView, BooksDetailView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books-all"),
    path('books/<int:pk>/edit', BooksDetailView.as_view(), name="book-update")
]
