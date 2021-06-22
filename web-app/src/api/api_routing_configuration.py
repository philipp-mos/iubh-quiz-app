from flask import current_app as app

from .v1 import admin, subjects


app.register_blueprint(admin.api_v1__admin_controller)
app.register_blueprint(subjects.api_v1__subjects_controller)
