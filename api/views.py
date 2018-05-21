from rest_framework import generics, status
from rest_framework.response import Response

from api.serializers import BooksSerializer
from catalog.models import Book


class ListBooksView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT songs/:id/
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

    def put(self, request, *args, **kwargs):
        try:
            a_book = self.queryset.get(pk=kwargs["pk"])
            serializer = BooksSerializer()
            updated_book = serializer.update(a_book, request.data)
            return Response(BooksSerializer(updated_book).data)
        except Book.DoesNotExist:
            return Response(
                data={
                    "message": "Book with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
