from django.urls import path, re_path

import knihovna
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='kniha-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('genres/', views.GenresListView.as_view(), name='genres'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('genres/create/', views.GenreCreate.as_view(), name='genre-create'),
    path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genre-delete'),
    path('authors/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
