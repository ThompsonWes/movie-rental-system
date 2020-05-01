# main.py

from flask import render_template
from app import app
from models import create_db

create_db()


@app.route('/')
@app.route('/login')
def login():
    """
    Render Login.html
    """
    return render_template('Login.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
