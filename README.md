# google books api
Simple python wrapper for google books api

## Install dependencies
```
pip install -r requirements.txt
```

## Example

```python
import google_book_api

# get volume using volume id
volume_id = 'MDksDwAAQBAJ'
volume = google_book_api.get_volume(volume_id)

# list books by search query
# see https://developers.google.com/books/docs/v1/using#PerformingSearch for search params
query = 'isbn:9781473539600'
response = google_book_api.list_books(query)
```


