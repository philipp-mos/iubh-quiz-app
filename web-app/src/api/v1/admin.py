from flask import current_app as app
from flask import Blueprint, jsonify, request
from flask_migrate import upgrade
from os import path


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


@api_v1__admin_controller.route('/app-version', methods=['GET'])
def get_appversion():

    version_number = '0.0.0'

    version_file_path = path.join(app.root_path, '../version.txt')

    try:
        with app.open_resource(version_file_path, 'r') as version_file:
            version_number = version_file.read()
    except FileNotFoundError:
        print(version_file_path + ' does not exist')

    return jsonify({ 'version': version_number })