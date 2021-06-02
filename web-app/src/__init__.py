import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()

login_manager = LoginManager()


def create_app():

    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder = "templates",
        static_folder = "static"
    )

    app.config.from_object('config.Config')

    logging_handler = RotatingFileHandler('logs/app.log', backupCount=15, maxBytes=10000000)
    logging_handler.setLevel(logging.INFO)
    logging_formatter = logging.Formatter("[%(levelname)s] [%(asctime)s] %(message)s {%(pathname)s:%(lineno)d}")
    logging_handler.setFormatter(logging_formatter)
    app.logger.addHandler(logging_handler)

    db.init_app(app)

    migrate = Migrate(app, db)

    login_manager.init_app(app)


    with app.app_context():
        from .services.UserService import UserService

        from .template_extensions import error_handlers, context_preprocessors

        from .models import model_registration

        from .api import api_routing_configuration

        from .modules import routing_configuration


        return app
