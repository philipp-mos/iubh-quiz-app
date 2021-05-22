from flask import current_app as app


from . import subjects
app.register_blueprint(subjects.api_v1__subjects_controller)