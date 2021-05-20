import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, "antenv"))
# basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_APP = 'app.py'

    SECRET_KEY = os.environ.get("SECRET_KEY")
    # SECRET_KEY = os.getenv("SECRET_KEY")

    FLASK_ENV = os.environ.get("FLASK_ENV", "development")
    # FLASK_ENV = os.getenv("FLASK_ENV", "development")

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

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
