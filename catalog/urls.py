from django.urls import path
from django.views import generic

from catalog import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
]
