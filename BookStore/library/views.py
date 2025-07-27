from django.db.models import Count, Q
from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm
from django.views.generic import ListView
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'all_books.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.select_related('author', 'genre').all()


def book_search_view(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        author_query = form.cleaned_data.get('author')
        genre = form.cleaned_data.get('genre')

        if author_query:
            books = books.filter(
                Q(author__first_name__icontains=author_query) |
                Q(author__last_name__icontains=author_query)
            )

        if genre:
            books = books.filter(genre=genre)

    genre_stats = books.values('genre__category').annotate(total=Count('id')).order_by('-total')

    return render(request, 'search.html', {
        'form': form,
        'books': books,
        'genre_stats': genre_stats,
    })



