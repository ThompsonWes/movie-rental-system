# models.py

from app import db

# each class will create a table in the database


class User(db.Model):
    """
    Users Entity
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class CreditCard(db.Model):
    """
    Credit Card Entity
    """
    cc_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cc_number = db.Column(db.String(16), index=True, nullable=False)
    cc_company = db.Column(db.String(64), index=True, nullable=False)
    cc_expiration = db.Column(db.Date, index=True, nullable=False)
    cc_cvc = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<CC {}>'.format(self.body)


def create_db():
    """
    Creates the database instance
    """
    db.create_all()


