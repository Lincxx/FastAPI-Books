from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'title 1', 'author': 'author 1', 'category': 'science'},
    {'title': 'title 2', 'author': 'author 2', 'category': 'science'},
    {'title': 'title 3', 'author': 'author 3', 'category': 'history'},
    {'title': 'title 4', 'author': 'author 4', 'category': 'math'},
    {'title': 'title 5', 'author': 'author 5', 'category': 'math'},
    {'title': 'title 6', 'author': 'author 2', 'category': 'math'},
]


@app.get("/books") 
async def read_all_books():
    return BOOKS

# @app.get("/books/mybook")
# async def read_all_books():
#     return {'book title': 'My fav book'}

# path parameters - ie http://localhost:8000/books/mybook
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book



# query parameters - ie http://localhost:8000/books/?category=math
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []

    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

# path and query parameters - ie http://localhost:8000/books/author_name/?category=category
@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []

    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
           book.get('category').casefold() == category.casefold() :
            books_to_return.append(book)

    return books_to_return