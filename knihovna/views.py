from django.shortcuts import render
from knihovna.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


def error_404(request, exception):
    data = {}
    return render(request, 'error/404.html', data)


def error_403(request, exception):
    data = {}
    return render(request, 'error/403.html', data)


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


class BookCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name', 'genre', 'author', 'date', 'pages', 'rate', 'isbn', 'image']
    permission_required = 'knihovna.can_add_books'

    def get_success_url(self):
        return reverse_lazy('books')


class BookUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'knihovna.can_update_books'


class BookDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'knihovna.can_delete_books'


class GenreCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Genre
    fields = ['name']
    permission_required = 'knihovna.can_add_genres'

    def get_success_url(self):
        return reverse_lazy('genres')


class GenreUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Genre
    fields = '__all__'
    permission_required = 'knihovna.can_update_genres'


class GenreDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy('genres')
    permission_required = 'knihovna.can_delete_genres'


class AuthorCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']
    permission_required = 'knihovna.can_add_authors'

    def get_success_url(self):
        return reverse_lazy('authors')


class AuthorUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    permission_required = 'knihovna.can_update_authors'


class AuthorDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'knihovna.can_delete_authors'
