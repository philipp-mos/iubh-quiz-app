import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from managers.CacheManager import CacheManager


db = SQLAlchemy()

login_manager = LoginManager()

cache_manager = CacheManager()


def create_app():

    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object('config.Config')

    logging_handler = RotatingFileHandler('logs/app.log', backupCount=15, maxBytes=10000000)
    logging_handler.setLevel(logging.INFO)
    logging_formatter = logging.Formatter("[%(levelname)s] [%(asctime)s] %(message)s {%(pathname)s:%(lineno)d}")
    logging_handler.setFormatter(logging_formatter)
    app.logger.addHandler(logging_handler)

    db.init_app(app)

    migrate = Migrate(app, db)  # noqa: F841

    login_manager.init_app(app)
    login_manager.session_protection = "basic"

    with app.app_context():
        from .services.UserService import UserService  # noqa: F401

        from .template_extensions import error_handlers, context_preprocessors  # noqa: F401

        from .models import model_registration  # noqa: F401

        from .api import api_routing_configuration  # noqa: F401

        from .modules import routing_configuration  # noqa: F401

        return app
