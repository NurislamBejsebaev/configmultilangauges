import factory
from core.factories import BookFactory
from .models import Reader, BookReading


class ReaderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reader

    name = factory.Faker('name')
    email = factory.Faker('email')


class BookReadingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BookReading

    book = factory.SubFactory(BookFactory)
    reader = factory.SubFactory(ReaderFactory)
    date_read = factory.Faker('date')
