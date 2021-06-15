from django.shortcuts import render
from knihovna.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    books = Book.objects.order_by('-rate')[:3]

    context = {
        'num_books': num_books,
        'books': books
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = "book"


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "author_list"
    paginate_by = 10


class GenresListView(generic.ListView):
    model = Genre
    context_object_name = "genre_list"
    paginate_by = 10


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'genre', 'author', 'date', 'pages', 'rate', 'isbn']
    initial = {'date': '15/06/2020'}


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
