# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Establishes the URI of the database
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'mrs.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
