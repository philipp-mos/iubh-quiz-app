from flask import current_app as app
from flask_swagger_ui import get_swaggerui_blueprint


swaggerui_controller = get_swaggerui_blueprint(
    app.config.get('SWAGGERUI_API_PATH'),
    app.config.get('SWAGGERUI_CONFIGURATION_LOCATION'),
    config={
        'app_name': 'iuquiz'
    }
)
