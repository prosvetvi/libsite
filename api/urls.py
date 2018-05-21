from django.urls import path

from api.views import ListBooksView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books-all")
]
