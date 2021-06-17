from flask import current_app as app


from .auth import auth
app.register_blueprint(auth.auth_controller)

from .legal import legal
app.register_blueprint(legal.legal_controller)

from .home import home
app.register_blueprint(home.home_controller)

from .subjects import subjects
app.register_blueprint(subjects.subjects_controller)

from .suggestquestion import suggestquestion
app.register_blueprint(suggestquestion.suggestquestion_controller)

from .user import user
app.register_blueprint(user.user_controller)