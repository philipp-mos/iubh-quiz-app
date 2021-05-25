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

    db.init_app(app)

    migrate = Migrate(app, db)

    login_manager.init_app(app)


    with app.app_context():
        from .services.UserService import UserService

        from .template_extensions import error_handlers
        from .template_extensions import context_preprocessors

        from .api.v1 import api_routing_configuration

        from .modules import routing_configuration


        return app
