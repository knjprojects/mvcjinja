import csv
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.database import db
from App.controllers import create_user
from App.controllers import login, create_book, create_review
index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    db.drop_all()
    db.create_all()
    bob=create_user('bob', 'bobpass')
    create_book('The Hobbit', 'J.R.R. Tolkien', 'George Allen & Unwin','https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FThe_Hobbit_%2528film_series%2529&psig=AOvVaw3lI_iZvup8UOSgMlCbAjzf&ust=1712638446482000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLi-hsTpsYUDFQAAAAAdAAAAABAE')
    #create_review(1,1,3,'Great!')
    bob.review_book(1, 3,'A great book!')
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    #db.drop_all()
    #db.create_all()
    #bob=create_user('bob', 'bobpass')
    #login('bob','bobpass')
    #create_user('bob', 'bobpass')
    #create_book('The Hobbit', 'J.R.R. Tolkien', 'George Allen & Unwin')
    #bob.review_book(1, 1, 'A great book!')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

"""@index_views.route('/api/data')
def get_data():
    response = index_views.open('https://amiiboapi.com/api/amiibo/?showusage').json()#requests.get('https://amiiboapi.com/api/amiibo/?showusage')
    data = response.json()
    return jsonify(data.amiibo)
    """