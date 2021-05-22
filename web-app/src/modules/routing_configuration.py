from flask import current_app as app


from .home import home
app.register_blueprint(home.home_controller)
