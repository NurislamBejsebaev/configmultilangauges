from django.db import models
from core.models import Book


class Reader(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя читателя')
    email = models.EmailField(unique=True, verbose_name='Email')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


class BookReading(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='readers', verbose_name='Книга')
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='books_read', verbose_name='Читатель')
    date_read = models.DateField(verbose_name='Дата прочтения')

    def __str__(self):
        return f'{self.reader} прочитал(а) "{self.book}"'

    class Meta:
        verbose_name = 'Прочтение книги'
        verbose_name_plural = 'Прочтения книг'