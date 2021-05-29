import os
from dotenv import load_dotenv


class Config(object):

    basedir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(basedir, '.env'))

    FLASK_APP = 'app.py'

    SECRET_KEY = os.environ.get("SECRET_KEY")

    FLASK_ENV = os.environ.get("FLASK_ENV")

    MIGRATION_KEY = os.environ.get("MIGRATION_KEY")

    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRESQLCONNSTR_APPDB")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_TAGMANAGER_ACTIVE = (os.environ.get("GOOGLE_TAGMANAGER_ACTIVE") == 'True')
    GOOGLE_TAGMANAGER_KEY = os.environ.get("GOOGLE_TAGMANAGER_KEY")


    if FLASK_ENV == 'development':
        DEBUG = True
        TESTING = True
        SQLALCHEMY_ECHO = True
    elif FLASK_ENV == 'staging':
        TESTING = True
