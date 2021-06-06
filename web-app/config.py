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

    # Database Settings
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRESQLCONNSTR_APPDB")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEFAULT_RESULT_ITEM_MAX_COUNT = 100

    # Google Tag Manager
    GOOGLE_TAGMANAGER_ACTIVE = (os.environ.get("GOOGLE_TAGMANAGER_ACTIVE") == 'True')
    GOOGLE_TAGMANAGER_KEY = os.environ.get("GOOGLE_TAGMANAGER_KEY")

    # Google ReCaptcha v3
    IS_GOOGLE_RECAPTCHA_ACTIVE = (os.environ.get("IS_GOOGLE_RECAPTCHA_ACTIVE") == 'True')
    GOOGLE_RECAPTCHA_SITEKEY = os.environ.get("GOOGLE_RECAPTCHA_SITEKEY")
    GOOGLE_RECAPTCHA_SECRETKEY = os.environ.get("GOOGLE_RECAPTCHA_SECRETKEY")
    GOOGLE_RECAPTCHA_SITEVERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'

    # Signup Process
    IS_SIGNUP_EMAIL_VALIDATION_ACTIVE = (os.environ.get("IS_SIGNUP_EMAIL_VALIDATION_ACTIVE") == 'True')
    USER_SIGNUP_EMAIL_LIMITATION = os.environ.get("USER_SIGNUP_EMAIL_LIMITATION")

    # UserRoles
    USERROLE_STUDENT = 1
    USERROLE_TUTOR = 2


    if FLASK_ENV == 'development':
        DEBUG = True
        TESTING = True
        SQLALCHEMY_ECHO = True
    elif FLASK_ENV == 'staging':
        TESTING = True
