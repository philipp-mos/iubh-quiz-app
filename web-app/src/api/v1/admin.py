from flask import current_app as app
from flask import Blueprint, jsonify, request
from flask_migrate import upgrade



api_v1__admin_controller = Blueprint(
    'api_v1__admin_controller',
    __name__,
    url_prefix='/api/v1/admin'
)


@api_v1__admin_controller.route('/run-migrations', methods=['GET'])
def run_migrations():

    if request.args.get('migrationkey') == app.config['MIGRATION_KEY']:
        upgrade(directory="./migrations")
        
        return jsonify({ 'status': 'success' }), 200

    return jsonify({ 'status': 'denied' }), 403
