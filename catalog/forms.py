from django.forms import ModelForm, DateTimeInput

from catalog.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title', "author", "image", "file", "read_date", "can_download")
        widgets = {
            'read_date': DateTimeInput(format='%Y-%m-%d %H:%M', attrs={
                'class': 'datepicker'}),
        }
