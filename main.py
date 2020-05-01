# main.py

from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from db_setup import init_db

# create the database
init_db()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# create routes for the web app


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
