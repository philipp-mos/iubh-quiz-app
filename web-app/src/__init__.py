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

    @app.context_processor
    def inject_bundle_version():
        return dict(bundle_version='')

    with app.app_context():

        from .api.v1 import subjects
        app.register_blueprint(subjects.api_v1__subjects_controller)
        
        from .modules.home import home
        app.register_blueprint(home.home_controller)

        return app
