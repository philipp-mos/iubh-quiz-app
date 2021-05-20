import os
from dotenv import load_dotenv


class Config(object):

    FLASK_APP = 'app.py'

    FLASK_ENV = 'development'

    DEBUG = False
    TESTING = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    if FLASK_ENV == 'development' :
        DEBUG = True
        TESTING = True
        SQLALCHEMY_ECHO = True
    elif FLASK_ENV == 'staging' :
        TESTING = True



class ConfigLocal(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, "antenv"))

    SECRET_KEY = os.environ.get("SECRET_KEY")

    FLASK_ENV = os.environ.get("FLASK_ENV", "development")

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")




class ConfigDocker(Config):

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.getenv("SECRET_KEY")

    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
