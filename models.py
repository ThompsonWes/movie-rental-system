# models.py

from main import db

# each class will create a table in the database


class User(db.Model):
    """
    Users Entity
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    dob = db.Column(db.Date)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class CreditCard(db.Model):
    """
    Credit Card Entity
    """
    cc_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cc_number = db.Column(db.String(16), index=True)
    cc_company = db.Column(db.String(64), index=True)
    cc_expiration = db.Column(db.Date, index=True)
    cc_cvc = db.Column(db.Integer)

    def __repr__(self):
        return '<CC {}>'.format(self.body)
