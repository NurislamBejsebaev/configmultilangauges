from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=50, verbose_name='Автор')
    publication_date = models.DateField(verbose_name='Дата публикации')
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    language = models.CharField(max_length=20, verbose_name='Язык')
    page_count = models.PositiveIntegerField(verbose_name='Количество страниц')
    cover_image = models.ImageField(upload_to='book_covers/', verbose_name='Обложка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
