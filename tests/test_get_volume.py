import unittest
import google_book_api
from requests.exceptions import HTTPError


class TestGetBooks(unittest.TestCase):
    def test_get_volume_1(self):
        volume_id = 'MDksDwAAQBAJ'
        volume_title = 'Ikigai'
        volume = google_book_api.get_volume(volume_id)
        self.assertEqual(volume['volumeInfo']['title'], volume_title)

    def test_get_volume_404(self):
        volume_id = '3333DksDwAAQBAJd'
        with self.assertRaises(HTTPError):
            google_book_api.get_volume(volume_id)


if __name__ == '__main__':
    unittest.main()
