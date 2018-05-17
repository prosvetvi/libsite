from django.contrib import admin
from catalog.models import Book, Author, BookReading

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookReading)
