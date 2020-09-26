import unittest
import google_book_api


class TestListBooks(unittest.TestCase):
    def test_list_books_1(self):
        query = 'isbn:9781473539600'
        volume_title = 'Ikigai'
        response = google_book_api.list_books(query)

        self.assertTrue(response['totalItems'] >= 1)
        self.assertEqual(response['items'][0]['volumeInfo']['title'], volume_title)

    def test_list_books_2(self):
        query = 'isbn:9781473539600xxxx'

        response = google_book_api.list_books(query)

        self.assertTrue(response['totalItems'] == 0)


if __name__ == '__main__':
    unittest.main()
