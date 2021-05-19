import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_APP = 'app.py'

    SECRET_KEY = os.getenv("SECRET_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = False
    TESTING = False

    if FLASK_ENV == 'development' :
        DEBUG = True
        TESTING = True
        SQLALCHEMY_ECHO = True
    elif FLASK_ENV == 'staging' :
        TESTING = True
