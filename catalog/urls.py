from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('create/book', views.BookCreate.as_view(), name='create_book'),
]
