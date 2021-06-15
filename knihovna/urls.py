from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='kniha-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('genres/', views.GenresListView.as_view(), name='genres'),
]
