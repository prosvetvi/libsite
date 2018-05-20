from django.views import generic
from django.core.cache import cache
from django.views.generic import CreateView

from catalog.forms import BookForm
from catalog.models import Book


class BookListView(generic.ListView):
    """
    Generic class-based view for a list of books.
    """
    template_name = 'catalog/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        """
        Return the last reading books.
        """
        return cache.get_or_set('last_book_list', Book.objects.order_by('-read_date')[:3], 24 * 60 * 60)


class BookCreate(CreateView):
    form_class = BookForm
    model = Book

