from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'titele 1', 'author': 'author 1', 'category': 'science'},
    {'title': 'titele 2', 'author': 'author 2', 'category': 'science'},
    {'title': 'titele 3', 'author': 'author 3', 'category': 'history'},
    {'title': 'titele 4', 'author': 'author 4', 'category': 'math'},
    {'title': 'titele 5', 'author': 'author 5', 'category': 'math'},
    {'title': 'titele 6', 'author': 'author 2', 'category': 'math'},
]


@app.get("/books") 
async def read_all_books():
    return BOOKS


# @app.get("/api-endpoint") 
# async def fast_api():
#     return BOOKS