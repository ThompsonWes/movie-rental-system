# main.py

from flask import render_template, request, make_response
from flask_cors import CORS, cross_origin
from app import app, db
from models import User
import datetime

db.create_all()


@app.route('/')
@app.route('/login')
def login():
    """
    Render Login.html
    """
    return render_template('Login.html')


@app.route('/', methods=['GET'])
@cross_origin(allow_headers=['Content-Type'])
def validate():

    return None


@app.route('/createUser', methods=['GET'])
def create_user():
    username = 'funkjo'
    password = 'password'
    email = 'funkjo@my.easternct.edu'
    dob = datetime.datetime(1998, 9, 12)
    new_user = User(username=username, email=email, password_hash=password, dob=dob)
    db.session.add(new_user)
    db.session.commit()
    return make_response(f"{new_user} successfully created!")


if __name__ == '__main__':
    app.run(debug=True)
