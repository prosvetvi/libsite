from rest_framework import serializers
from catalog.models import Book


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author", "read_date")
