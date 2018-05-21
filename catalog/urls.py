from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('book/add', views.BookCreate.as_view(success_url="/catalog/"), name='create_book'),
    path('book/<int:pk>', views.BookUpdate.as_view(success_url="/catalog/"), name='update_book'),
]
