from App.models import User
from App.models import Book
from App.models import Review
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
def review_book(User, book_id, rating, reviewtext):
        book = Book.query.get(book_id)
        if book:
            try:
                review = Review(User.id, book_id, reviewtext, rating)
                db.session.add(review)
                db.session.commit()
                return review
            except Exception as e:
                print(e)
                db.session.rollback()
                return None
        return None

def delete_review(User, review_id):
    review = Review.query.get(review_id)
    if review.user == User:
        db.session.delete(review)
        db.session.commit()
        return True
    return None

def update_review(User, review_id, reviewtext, rating):
    review = Review.query.get(review_id)
    if review.user == User:
      review.reviewtext = reviewtext
      review.rating = rating
      db.session.add(review)
      db.session.commit()
      return True
    return None
def signUpUser(username,password):
    newuser = create_user(username=username,
                      
                        password=password)  # create user object
    
    try:
        db.session.add(newuser)
        db.session.commit()  # save user
        return newuser
        
    except Exception:  # attempted to insert a duplicate user
        db.session.rollback()
        # error message
    return None