from rest_framework import status
from rest_framework.test import APITestCase
from .factories import BookFactory


class BookAPITestCase(APITestCase):

    def test_create_book(self):
        data = {
            "title": "Sample Book",
            "author": "John Doe",
            "publication_date": "2023-01-01",
            "isbn": "1234567890123",
            "genre": "Fiction",
            "language": "English",
            "page_count": 300,
        }
        response = self.client.post('/books/books/', data, format='multipart')

        # Распечатайте тело ответа для получения дополнительных сведений об ошибке.
        # print(response.content.decode())
        # Это выведет информацию о теле ответа в консоль.

        # Добавьте отладочные утверждения для анализа проблемы.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_get_book_list(self):
        BookFactory.create_batch(5)
        response = self.client.get('/books/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_get_book_detail(self):
        book = BookFactory()
        response = self.client.get(f'/books/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        book = BookFactory()
        data = {
            "title": "Updated Title",
            "author": "Updated Author",
            "publication_date": "2023-02-01",
            "isbn": "1234567890156",
            "genre": "New genre",
            "language": "Russian",
            "page_count": 301
        }
        response = self.client.put(f'/books/books/{book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")
        self.assertEqual(response.data["author"], "Updated Author")

    def test_partial_update_book(self):
        book = BookFactory()
        data = {
            "title": "Updated Title"
        }
        response = self.client.patch(f'/books/books/{book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        book = BookFactory()
        response = self.client.delete(f'/books/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
