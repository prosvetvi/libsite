from django.forms import ModelForm, SplitDateTimeWidget

from catalog.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', "authors", "image", "file", "read_date", "can_download")
        widgets = {
            'read_date': SplitDateTimeWidget(date_format='%d/%m/%Y'),
        }
