from main import db
from models import User


def test():
    u = User(username='test', email='test', password_hash='test', dob='test')
    db.session.add(u)
    db.session.commit()


test()




