from App.models import Book
from App.database import db
from flask import jsonify
def create_book( name, author, publisher):
    newbook = Book(name=name, author=author, publisher=publisher)
    db.session.add(newbook)
    db.session.commit()
    return newbook

def get_book_by_name(name):
    return Book.query.filter_by(name=name).first()

def get_book(id):
    return Book.query.get(id)

def get_all_books():
    return Book.query.all()

def get_all_books_json():
    books = Book.query.all()
    if not books:
        return []
    books = [book.get_json() for book in books]
    return books
def get_complete_books_data():
    data=[]
    books = Book.query.all()
    for book in books:
        total_rating = sum([review.rating for review in book.reviews])
        average_rating = total_rating / len(book.reviews)
        data.append({
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'publisher': book.publisher,
            'average_rating': average_rating,
            'reviews_count': len(book.reviews)
        })
    return jsonify(data)
         
"""def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    """
    