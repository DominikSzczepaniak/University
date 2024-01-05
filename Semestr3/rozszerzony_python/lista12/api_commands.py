import requests 

API_URL = "http://127.0.0.1:5000/"

def list_books():
    response = requests.get(API_URL + "books")
    print(response.json())

def get_book(book_id):
    response = requests.get(API_URL + "books/" + str(book_id))
    print(response.json())

def add_book(title, year, author):
    data = {
        'title': title,
        'year': year,
        'author': author
    }
    response = requests.post(API_URL + "books", json=data)
    print(response.json())

def delete_book(book_id):
    response = requests.delete(API_URL + "books/" + str(book_id))
    print(response.json())
