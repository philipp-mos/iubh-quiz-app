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
    """
    Run Migrations, if correct MigrationKey is transmitted
    Returns Status
    """

    if request.args.get('migrationkey') == app.config['MIGRATION_KEY']:
        upgrade(directory="./migrations")

        app.logger.info('Migration successfully executed')
        return jsonify({'status': 'success'}), 200

    app.logger.warning('Failed Authentication due to wrong Migration-Key')
    return jsonify({'status': 'denied'}), 403


@api_v1__admin_controller.route('/app-version', methods=['GET'])
def get_appversion():
    """
    Returns the current Application-Version as JSON
    """

    version_number = '0.0.0'

    version_file_path = path.join(app.root_path, '../version.txt')

    try:
        with app.open_resource(version_file_path, 'r') as version_file:
            version_number = version_file.read()
    except FileNotFoundError:
        app.logger.error('version.txt does not exist')

    return jsonify({'version': version_number}), 200
