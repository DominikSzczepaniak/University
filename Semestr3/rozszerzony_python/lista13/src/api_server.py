from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from flask import Flask, jsonify, request
import argparse

app = Flask(__name__)
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


engine = create_engine(
    'postgresql://lista11:lista11@localhost:5432/library_db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def book_to_dict(book):
    return {
        'id': book.id,
        'title': book.title,
        'year': book.year,
        'author': book.author.name,
        'friend': book.friend.name if book.friend else None
    }


@app.route('/books', methods=['GET'])
def get_books():
    books = session.query(Book).all()
    return jsonify([book_to_dict(book) for book in books])


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        return jsonify(book_to_dict(book))
    else:
        return jsonify({'error': 'Book not found'}), 404


@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    title = data.get('title')
    year = data.get('year')
    author_name = data.get('author')

    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    book = Book(title=title, year=year, author=author)
    session.add(book)
    session.commit()

    return jsonify(book_to_dict(book)), 201


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    session = Session()
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        session.close()
        return jsonify({'message': 'Book deleted successfully'})
    else:
        session.close()
        return jsonify({'error': 'Book not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
