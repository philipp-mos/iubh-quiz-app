from flask import current_app as app
from os import path

from .. import cache_manager


@app.context_processor
def inject_app_version():
    """Reads from version.txt to inject app_version to Views"""
    version_number = cache_manager.get_from_key(cache_manager._APPVERSION)

    if version_number:
        return dict(app_version=version_number)

    version_file_path = path.join(app.root_path, '../version.txt')

    try:
        with app.open_resource(version_file_path, 'r') as version_file:
            version_number = version_file.read()
            cache_manager.set_by_key(cache_manager._APPVERSION, version_number, cache_manager._ONEDAY)
    except FileNotFoundError:
        app.logger.error('version.txt does not exist')

    return dict(app_version=version_number)


@app.context_processor
def inject_bundle_version():
    """Reads bundle-version.txt to inject bundle_version to Views"""
    version_number = ''

    try:
        with app.open_resource('static/bundle-version.txt', 'r') as version_file:
            version_number = version_file.read()
    except FileNotFoundError:
        app.logger.error('bundle-version.txt does not exist')

    return dict(bundle_version=version_number)
