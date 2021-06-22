from flask import current_app as app
from flask import Blueprint, jsonify, request
from flask_migrate import upgrade
from os import path

from ... import cache_manager

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

    version_number = cache_manager.get_from_key(cache_manager._APPVERSION)

    if version_number:
        return jsonify({'version': version_number}), 200

    version_file_path = path.join(app.root_path, '../version.txt')

    try:
        with app.open_resource(version_file_path, 'r') as version_file:
            version_number = cache_manager.set_by_key(cache_manager._APPVERSION, version_file.read(), cache_manager._ONEDAY)
    except FileNotFoundError:
        app.logger.error('version.txt does not exist')

    return jsonify({'version': version_number}), 200


@api_v1__admin_controller.route('/purge-app-cache', methods=['GET'])
def purge_app_cache():
    """
    Deletes the App-Cache Value
    """

    if request.args.get('migrationkey') == app.config['MIGRATION_KEY']:
        cache_manager.purge_cache()

        return jsonify({'status': 'success'}), 200

    app.logger.warning('Failed Authentication due to wrong Migration-Key')
    return jsonify({'status': 'denied'}), 403
