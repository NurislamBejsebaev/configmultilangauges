from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название книги'))
    author = models.CharField(max_length=50, verbose_name=_('Автор'))
    publication_date = models.DateField(verbose_name=_('Дата публикации'))
    isbn = models.CharField(max_length=20, unique=True, verbose_name=_('ISBN'))
    genre = models.CharField(max_length=50, verbose_name=_('Жанр'))
    language = models.CharField(max_length=20, verbose_name=_('Язык'))
    page_count = models.PositiveIntegerField(verbose_name=_('Количество страниц'))
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True, verbose_name=_('Обложка'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
