# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

app = Flask(__name__)  # create flask app
CORS(app, supports_credentials=True)
app.config.from_object(Config)  # configures SQLALCHEMY_DATABASE_URI to sqlite:///mrs.db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mrs.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # create sqlalchemy database object from our flask app


# class User(db.Model):
#     """
#     Users Entity
#     """
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     dob = db.Column(db.Date, nullable=False)
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#
# class CreditCard(db.Model):
#     """
#     Credit Card Entity
#     """
#     cc_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     cc_number = db.Column(db.String(16), index=True, nullable=False)
#     cc_company = db.Column(db.String(64), index=True, nullable=False)
#     cc_expiration = db.Column(db.Date, index=True, nullable=False)
#     cc_cvc = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return '<CC {}>'.format(self.body)
