from django.urls import path
from .views import book_search_view, BookListView
app_name = 'library'
urlpatterns = [path('books/', BookListView.as_view(), name='all_books'),
               path('search/', book_search_view, name='search'),]