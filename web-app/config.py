from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, "antenv"))


class Config:
    FLASK_APP = 'app.py'

    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
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
