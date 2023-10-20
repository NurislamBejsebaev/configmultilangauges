import factory
from .models import Book


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker('sentence', nb_words=4)
    author = factory.Faker('name')
    publication_date = factory.Faker('date')
    isbn = factory.Faker('ean13')
    genre = factory.Faker('word')
    language = factory.Faker('language_code')
    page_count = factory.Faker('random_int', min=50, max=1000)

