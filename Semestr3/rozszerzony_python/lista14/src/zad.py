from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from src import api_commands
import argparse
import functools

Base = declarative_base()

def cache_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "cache"):
            wrapper.cache = {}
        key = (args, frozenset(kwargs.items()))
        if key in wrapper.cache:
            return wrapper.cache[key]
        result = func(*args, **kwargs)
        wrapper.cache[key] = result
        return result
    return wrapper

def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(args[0], 'is_logged_in', False):
            raise Exception("User must be logged in to use this function.")
        return func(*args, **kwargs)
    return wrapper

class Author(Base):  # type: ignore
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', back_populates='author')


class Book(Base):  # type: ignore
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', back_populates='books')
    friend_id = Column(Integer, ForeignKey('friends.id'))
    friend = relationship('Friend', back_populates='books')


class Friend(Base):  # type: ignore
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    books = relationship('Book', back_populates='friend')


engine = create_engine(
    'postgresql://lista11:lista11@localhost:5432/library_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_book(title: str, year: int, author_name: str):
    book = session.query(Book).join(Author).filter(
        Book.title == title, Book.year == year).first()
    if book:
        print("Book already in database.")
        return False
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()
        return True

    book = Book(title=title, year=year, author=author)
    session.add(book)
    session.commit()
    return True


def borrow_book(friend_name: str, book_title: str, book_year: int):
    friend = session.query(Friend).filter_by(name=friend_name).first()
    book = session.query(Book).join(Author).filter(
        Book.title == book_title, Book.year == book_year).first()
    if book is not None and friend is not None:
        if book not in friend.books and book.friend is None:
            friend.books.append(book)
            session.commit()
            print(f"{friend.name} borrowed {book.title} ({book.year})")
            return True
        else:
            owner_of_book = session.query(Friend).join(Book).filter(
                Book.title == book_title, Book.year == book_year).first()
            if (owner_of_book is not None):
                print("%s has %s (%s), he needs to return it first." %
                      (owner_of_book.name, book.title, book.year))
            else:
                print("Owner not found")
            return False
    else:
        print("Friend, book, or author not found.")
        return False


def return_book(friend_name: str, book_title: str, book_year: int):
    friend = session.query(Friend).filter_by(name=friend_name).first()
    book = session.query(Book).join(Author).filter(
        Book.title == book_title, Book.year == book_year).first()

    if friend and book and book in friend.books:
        friend.books.remove(book)
        session.commit()
        print(f"{friend.name} returned {book.title} ({book.year})")
        return True
    else:
        print("Friend, book, or author not found, or the book is not borrowed by the specified friend.")
        return False


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


def add_friend(name: str, email: str):
    friend = session.query(Friend).filter_by(name=name, email=email).first()
    if friend:
        print("Friend already in database.")
        return False
    friend = Friend(name=name, email=email)
    session.add(friend)
    session.commit()
    return True


def list_books_for_friends():
    friends = session.query(Friend).all()
    for friend in friends:
        print(f"{friend.name}'s books:")
        for book in friend.books:
            print(f"  - {book.title} ({book.year}) - {book.author.name}")

@login_required
def delete_data():
    session.query(Book).delete()
    session.query(Friend).delete()
    session.query(Author).delete()
    session.commit()


def delete_book(book_id: int):
    book = session.query(Book).filter_by(id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
        if book.title in get_book_id.cache:
            del get_book_id.cache[book.title]
        return True
    else:
        print("Book not found.")
        return False


def delete_friend(friend_id: int):
    friend = session.query(Friend).filter_by(id=friend_id).first()
    if friend:
        session.delete(friend)
        session.commit()
        if (friend.name, friend.email) in get_friend_id.cache:
            del get_friend_id.cache[(friend.name, friend.email)]
        return True
    else:
        print("Friend not found.")
        return False

@cache_decorator
def get_friend_id(friend_name: str, friend_email: str):
    friend = session.query(Friend).filter_by(
        name=friend_name, email=friend_email).first()
    if friend:
        return friend.id
    else:
        return None

@cache_decorator
def get_book_id(book_title: str, book_year: int, book_author: str):
    book = session.query(Book).join(Author).filter(
        Book.title == book_title, Book.year == book_year, Author.name == book_author).first()
    if book:
        return book.id
    else:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Book library")
    parser.add_argument('--api', action='store_true', help='Use API')
    subparsers = parser.add_subparsers(
        dest='command', help='Available commands')

    list_book_api = subparsers.add_parser('get_book', help='List all books')
    list_book_api.add_argument(
        '--book_id', required=True, help='ID of the book')

    delete_book_api = subparsers.add_parser(
        'delete_book', help='Delete a book')
    delete_book_api.add_argument(
        '--book_id', required=True, help='ID of the book')

    add_friend_parser = subparsers.add_parser(
        'add_friend', help='Add a new friend')
    add_friend_parser.add_argument(
        '--name', required=True, help='Name of the friend')
    add_friend_parser.add_argument(
        '--email', required=True, help='Email of the friend')

    list_friends_parser = subparsers.add_parser(
        'list_friends', help='List all friends')

    add_book_parser = subparsers.add_parser('add_book', help='Add a new book')
    add_book_parser.add_argument(
        '--title', required=True, help='Title of the book')
    add_book_parser.add_argument(
        '--year', required=True, type=int, help='Publishing year of the book')
    add_book_parser.add_argument(
        '--author', required=True, help='Author of the book')

    borrow_book_parser = subparsers.add_parser(
        'borrow_book', help='Borrow a book')
    borrow_book_parser.add_argument(
        '--friend_name', required=True, help='Name of the friend')
    borrow_book_parser.add_argument(
        '--book_title', required=True, help='Title of the book')
    borrow_book_parser.add_argument(
        '--book_year', required=True, type=int, help='Year of publication')

    return_book_parser = subparsers.add_parser(
        'return_book', help='Return a borrowed book')
    return_book_parser.add_argument(
        '--friend_name', required=True, help='Name of the friend')
    return_book_parser.add_argument(
        '--book_title', required=True, help='Title of the book')
    return_book_parser.add_argument(
        '--book_year', required=True, type=int, help='Year of publication')

    list_books_parser = subparsers.add_parser(
        'list_books', help='List all books')

    delete_data_parser = subparsers.add_parser('delete_all_data')

    args = parser.parse_args()
    if (args.api):
        if args.command == 'list_books':
            api_commands.list_books()
        elif args.command == 'get_book':
            api_commands.get_book(args.book_id)
        elif args.command == 'add_book':
            api_commands.add_book(args.title, args.year, args.author)
        elif args.command == 'delete_book':
            api_commands.delete_book(args.book_id)
        else:
            print("Wrong command. Use --help for more information.")
    else:
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
