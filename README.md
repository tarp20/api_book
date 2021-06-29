# api_book
 simple book API

Technology:

-Python3

-Django REST Framework


This App use Google Api Book external api_book
Only backend part
Functionality:

POST /db
Post all book from external API (Google Api Book)

Get /books 
Get all books from database 
You can filter and sort by 'published_date'


GET /books?author=Jan Kowalski
 Get all books of a given author

GET /books/<bookId>

display book by id(in database)

in this form:

{
    "title": "Hobbit czyli Tam i z powrotem",
    "authors": ["J. R. R. Tolkien"],
    "published_date": "2004",
    "categories": [
        "Baggins, Bilbo (Fictitious character)"
      ],
    "average_rating": 5,
    "ratings_count": 2,
    "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
}



