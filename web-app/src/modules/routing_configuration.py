from flask import current_app as app

from .auth import auth
from .legal import legal
from .home import home
from .suggestquestion import suggestquestion
from .user import user


app.register_blueprint(auth.auth_controller)
app.register_blueprint(legal.legal_controller)
app.register_blueprint(home.home_controller)
app.register_blueprint(suggestquestion.suggestquestion_controller)
app.register_blueprint(user.user_controller)
