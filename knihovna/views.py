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


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = "book"


class AuthorCreate(CreateView):
    model = Author
    fields = ['name']


class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')