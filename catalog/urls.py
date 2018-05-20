from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('create/book', views.BookCreate.as_view(success_url="/catalog/"), name='create_book'),
]
