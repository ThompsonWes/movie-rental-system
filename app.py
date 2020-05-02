# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

app = Flask(__name__)  # create flask app
CORS(app, supports_credentials=True)
app.config.from_object(Config)  # configures SQLALCHEMY_DATABASE_URI to sqlite:///mrs.db
db = SQLAlchemy(app)  # create sqlalchemy database object from our flask app
