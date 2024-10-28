from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ('-id',)
        db_table = 'author'


class BookModel(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    isbn = models.CharField(max_length=14)

    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='books')

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author.__str__()}"

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('-id',)
        db_table = 'book'
