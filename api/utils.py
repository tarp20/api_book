import requests
import json

from django.db import IntegrityError

from books.models import Book


def save_data(title):
    items = json.loads(requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={title}").content).get('items')
    for book in items:
        try:
            title = book['volumeInfo']['title']
        except KeyError:
            title = None

        try:
            authors = book['volumeInfo']['authors']
            authors = ','.join(authors)
        except KeyError:
            authors = None

        try:
            published_date = book['volumeInfo']['publishedDate']
        except KeyError:
            published_date = None

        try:
            categories = book['volumeInfo']['categories']
            categories = ',$'.join(categories)
        except KeyError:
            categories = None

        try:
            average_rating = book['volumeInfo']['averageRating']
        except KeyError:
            average_rating = None

        try:
            ratings_count = book['volumeInfo']['ratingsCount']
        except KeyError:
            ratings_count = None

        try:
            thumbnail = book['volumeInfo']['imageLinks']['thumbnail']
        except KeyError:
            thumbnail = None

        mapping = {
            'title': title,
            'authors': authors,
            'published_date': published_date,
            'categories': categories,
            'average_rating': average_rating,
            'ratings_count': ratings_count,
            'thumbnail': thumbnail,

        }
        try:
            Book.objects.create(**mapping)
        except IntegrityError:
            pass
