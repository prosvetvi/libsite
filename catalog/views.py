from django.views import generic
from django.core.cache import cache
from django.views.generic import CreateView

from catalog.forms import BookForm
from catalog.models import Book
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


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
        cache_last_book_list = cache.get('last_book_list')
        if cache_last_book_list:
            logger.info("use cache")
            return cache_last_book_list
        logger.info("not use cache")
        last_book_list = Book.objects.order_by('-read_date')[:3]
        cache.set('last_book_list', last_book_list, 24 * 60 * 60)
        return last_book_list


class BookCreate(CreateView):
    form_class = BookForm
    model = Book

