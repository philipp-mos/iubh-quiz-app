import os
from dotenv import load_dotenv


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))

    FLASK_APP = 'app.py'

    SECRET_KEY = os.environ.get("SECRET_KEY")

    FLASK_ENV = os.environ.get("FLASK_ENV")

    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    if FLASK_ENV == 'development' :
        DEBUG = True
        TESTING = True
        SQLALCHEMY_ECHO = True
    elif FLASK_ENV == 'staging' :
        TESTING = True
