from django.contrib import admin
from .models import AuthorModel, BookModel


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthdate', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name')
    list_filter = ('birthdate',)


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'created_at', 'updated_at')
    search_fields = ('title', 'isbn')
    list_filter = ('author',)
