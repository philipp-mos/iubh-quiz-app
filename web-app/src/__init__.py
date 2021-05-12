from flask import Flask

def create_app():

    app = Flask(
        __name__,
        instance_relative_config=False,
        template_folder = "views",
        static_folder = "static"
    )

    app.config.from_object('config.DevConfig')

    with app.app_context():
        from .modules.home import home

        app.register_blueprint(home.home_controller)

        return app
