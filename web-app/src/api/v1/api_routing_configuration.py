from flask import current_app as app


from . import admin
app.register_blueprint(admin.api_v1__admin_controller)

from . import subjects
app.register_blueprint(subjects.api_v1__subjects_controller)