from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


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


    with app.app_context():
        from .modules.home import home

        app.register_blueprint(home.home_controller)

        return app
