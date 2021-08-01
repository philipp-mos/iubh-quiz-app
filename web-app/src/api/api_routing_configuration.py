from flask import current_app as app

from .v1 import admin, subjects, highscore
from .swagger import swagger


app.register_blueprint(admin.api_v1__admin_controller)
app.register_blueprint(subjects.api_v1__subjects_controller)
app.register_blueprint(highscore.api_v1__highscore_controller)

if app.config.get('FLASK_ENV') != 'production':
    app.register_blueprint(swagger.swaggerui_controller)
