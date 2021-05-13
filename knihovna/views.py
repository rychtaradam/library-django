from django.shortcuts import render
from knihovna.models import *


def index(request):
    num_books = Book.objects.all().count()
    books = Book.objects.order_by('-rate')[:3]

    context = {
        'num_books' : num_books,
        'books' : books
    }

    return render(request, 'index.html', context=context)
