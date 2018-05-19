from django.views import generic

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
        return Book.objects.order_by('-read_date')[:3]
