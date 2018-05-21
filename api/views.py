from rest_framework import generics, status, permissions
from rest_framework.response import Response

from api.serializers import BooksSerializer
from catalog.models import Book, Author


class ListBooksView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    PUT books/:id/edit
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (permissions.IsAuthenticated,)

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


class CreateBookView(generics.CreateAPIView):
    """
    POST books/add
    """
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        a_book = Book.objects.create(
            title=request.data["title"],
            author=Author.objects.get(pk=request.data["author"]),
            read_date=request.data["read_date"]
        )
        return Response(
            data=BooksSerializer(a_book).data,
            status=status.HTTP_201_CREATED
        )
