from rest_framework import generics

from api.serializers import BooksSerializer
from catalog.models import Book


class ListBooksView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
