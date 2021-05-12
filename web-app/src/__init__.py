from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():

    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder = "templates",
        static_folder = "static"
    )

    app.config.from_object('config.DevConfig')

    db.init_app(app)


    with app.app_context():
        from .modules.home import home

        app.register_blueprint(home.home_controller)

        return app
