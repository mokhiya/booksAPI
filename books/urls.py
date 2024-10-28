from django.urls import path

from books.views import authors, books

app_name = 'books'

urlpatterns = [
    path('authors', authors.author_list_create, name='author-list-create'),
    path('', books.book_list_create, name='book-list-create'),

    path('authors/<int:pk>', authors.author_detail, name='author-detail'),
    path('<int:pk>', books.book_detail, name='book-detail'),
]
