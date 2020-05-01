# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)  # create flask app
app.config.from_object(Config)  # configures SQLALCHEMY_DATABASE_URI to sqlite:///mrs.db
db = SQLAlchemy(app)  # create sqlalchemy database object from our flask app
