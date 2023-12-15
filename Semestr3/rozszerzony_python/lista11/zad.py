from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

import argparse

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', back_populates='books')
    friend_id = Column(Integer, ForeignKey('friends.id'))
    friend = relationship('Friend', back_populates='books')

class Friend(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    books = relationship('Book', back_populates='friend')

engine = create_engine('postgresql://lista11:lista11@localhost:5432/library_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_book(title, year, author_name):
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    book = Book(title=title, year=year, author=author)
    session.add(book)
    session.commit()

def borrow_book(friend_name, book_title, book_year):
    friend = session.query(Friend).filter_by(name=friend_name).first()
    book = session.query(Book).join(Author).filter(Book.title == book_title, Book.year == book_year).first()
    if book and friend:
        if book not in friend.books and book.friend is None:
            friend.books.append(book)
            session.commit()
            print(f"{friend.name} borrowed {book.title} ({book.year})")
        else:
            owner_of_book = session.query(Friend).join(Book).filter(Book.title == book_title, Book.year == book_year).first()
            print(f"{owner_of_book.name} has {book.title} ({book.year}), he needs to return it first.")
    else:
        print("Friend, book, or author not found.")


def return_book(friend_name, book_title, book_year):
    friend = session.query(Friend).filter_by(name=friend_name).first()
    book = session.query(Book).join(Author).filter(Book.title == book_title, Book.year == book_year).first()

    if friend and book and book in friend.books:
        friend.books.remove(book)
        session.commit()
        print(f"{friend.name} returned {book.title} ({book.year})")
    else:
        print("Friend, book, or author not found, or the book is not borrowed by the specified friend.")


def list_books():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.id}. {book.title} ({book.year}) - {book.author.name}")
        if book.friend:
            print(f"   Borrowed by: {book.friend.name}")
        else:
            print("   Available")

def list_friends():
    friends = session.query(Friend).all()
    for friend in friends:
        print(f"{friend.id}. {friend.name} ({friend.email})")

def add_friend(name, email):
    friend = Friend(name=name, email=email)
    session.add(friend)
    session.commit()

def list_books_for_friends():
    friends = session.query(Friend).all()
    for friend in friends:
        print(f"{friend.name}'s books:")
        for book in friend.books:
            print(f"  - {book.title} ({book.year}) - {book.author.name}")

def delete_data():
    session.query(Book).delete()
    session.query(Friend).delete()
    session.query(Author).delete()
    session.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Book library")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    add_friend_parser = subparsers.add_parser('add_friend', help='Add a new friend')
    add_friend_parser.add_argument('--name', required=True, help='Name of the friend')
    add_friend_parser.add_argument('--email', required=True, help='Email of the friend')

    list_friends_parser = subparsers.add_parser('list_friends', help='List all friends')

    add_book_parser = subparsers.add_parser('add_book', help='Add a new book')
    add_book_parser.add_argument('--title', required=True, help='Title of the book')
    add_book_parser.add_argument('--year', required=True, type=int, help='Publishing year of the book')
    add_book_parser.add_argument('--author', required=True, help='Author of the book')

    borrow_book_parser = subparsers.add_parser('borrow_book', help='Borrow a book')
    borrow_book_parser.add_argument('--friend_name', required=True, help='Name of the friend')
    borrow_book_parser.add_argument('--book_title', required=True, help='Title of the book')
    borrow_book_parser.add_argument('--book_year', required=True, type=int, help='Year of publication')

    return_book_parser = subparsers.add_parser('return_book', help='Return a borrowed book')
    return_book_parser.add_argument('--friend_name', required=True, help='Name of the friend')
    return_book_parser.add_argument('--book_title', required=True, help='Title of the book')
    return_book_parser.add_argument('--book_year', required=True, type=int, help='Year of publication')


    list_books_parser = subparsers.add_parser('list_books', help='List all books')

    delete_data_parser = subparsers.add_parser('delete_all_data')

    args = parser.parse_args()

    if args.command == 'add_book':
        add_book(args.title, args.year, args.author)
    elif args.command == 'add_friend':
        add_friend(args.name, args.email)
    elif args.command == 'borrow_book':
        borrow_book(args.friend_name, args.book_title, args.book_year)
    elif args.command == 'return_book':
        return_book(args.friend_name, args.book_title, args.book_year)
    elif args.command == 'list_books':
        list_books()
    elif args.command == 'list_friends':
        list_friends()
    elif args.command == 'delete_all_data':
        delete_data()
    else:
        print("Wrong command. Use --help for more information.")
#przykladowy test na ktorym dzialalem

#python3 zad.py add_friend --name Jan --email jan@localhost
#python3 zad.py add_friend --name Marek --email marek@localhost
#python3 zad.py add_book --title "Pan Tadeusz" --year 1834 --author "Adam Mickiewicz"
#python3 zad.py list_friends 
#python3 zad.py list_books
#python3 zad.py borrow_book --friend_name Jan --book_title "Pan Tadeusz" --book_year 1834
#wypozyczenie przez Jana
#python3 zad.py list_books
#python3 zad.py borrow_book --friend_name Marek --book_title "Pan Tadeusz" --book_year 1834
#^ brak operacji - Jan ma ksiazke
#python3 zad.py return_book --friend_name Jan --book_title "Pan Tadeusz" --book_year 1834
# zwrot przez Jana
#python3 zad.py list_books


