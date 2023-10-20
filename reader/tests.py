from rest_framework import status
from rest_framework.test import APITestCase
from .factories import BookFactory, ReaderFactory, BookReadingFactory


class ReaderAPITestCase(APITestCase):
    def test_create_reader(self):
        data = {
            "name": "Alice",
            "email": "alice@example.com"
        }
        response = self.client.post('/readers/readers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reader_list(self):
        ReaderFactory.create_batch(5)
        response = self.client.get('/readers/readers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_get_reader_detail(self):
        reader = ReaderFactory()
        response = self.client.get(f'/readers/readers/{reader.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_reader(self):
        reader = ReaderFactory()
        data = {
            "name": "Updated Name",
            "email": "updated@example.com"
        }
        response = self.client.put(f'/readers/readers/{reader.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Name")
        self.assertEqual(response.data["email"], "updated@example.com")

    def test_partial_update_reader(self):
        reader = ReaderFactory()
        data = {
            "name": "Updated Name"
        }
        response = self.client.patch(f'/readers/readers/{reader.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Name")

    def test_delete_reader(self):
        reader = ReaderFactory()
        response = self.client.delete(f'/readers/readers/{reader.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookReadingAPITestCase(APITestCase):
    def test_create_book_reading(self):
        book = BookFactory()
        reader = ReaderFactory()
        data = {
            "book": book.id,
            "reader": reader.id,
            "date_read": "2023-01-15"
        }
        response = self.client.post('/readers/bookreading/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book_reading_list(self):
        BookReadingFactory.create_batch(5)
        response = self.client.get('/readers/bookreading/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_get_book_reading_detail(self):
        book_reading = BookReadingFactory()
        response = self.client.get(f'/readers/bookreading/{book_reading.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_reading(self):
        book = BookFactory()
        reader = ReaderFactory()
        book_reading = BookReadingFactory()
        data = {
            'book': book.id,
            'reader': reader.id,
            "date_read": "2023-01-20"
        }
        response = self.client.put(f'/readers/bookreading/{book_reading.id}/', data, format='json')
        # print(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["date_read"], "2023-01-20")

    def test_partial_update_book_reading(self):
        book_reading = BookReadingFactory()
        data = {
            "date_read": "2023-01-25"
        }
        response = self.client.patch(f'/readers/bookreading/{book_reading.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["date_read"], "2023-01-25")

    def test_delete_book_reading(self):
        book_reading = BookReadingFactory()
        response = self.client.delete(f'/readers/bookreading/{book_reading.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
