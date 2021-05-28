from flask import current_app as app


from .auth import auth
app.register_blueprint(auth.auth_controller)

from .home import home
app.register_blueprint(home.home_controller)
