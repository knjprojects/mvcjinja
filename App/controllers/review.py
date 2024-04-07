from App.models import Review
from App.database import db



def get_review(id):
    return Review.query.get(id) #Review.query.filter_by(id=id).first()

def get_all_reviews():
    return Review.query.all()

def get_all_reviews_json():
    reviews = Review.query.all()
    if not reviews:
        return []
    reviews = [review.get_json() for review in reviews]
    return reviews

def get_book_reviews(book_id):
    return Review.query.filter_by(book_id=book_id).all()#Review.book.has(Book.name == book_name

def get_user_reviews(user_id):
    return Review.query.filter_by(user_id=user_id).all()

"""def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    """
    