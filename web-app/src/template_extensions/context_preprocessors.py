from flask import current_app as app
from os import path

@app.context_processor
def inject_app_version():
    """Reads from version.txt to inject app_version to Views"""
    version_number = '0.0.0'

    version_file_path = path.join(app.root_path, '../version.txt')

    try:
        with app.open_resource(version_file_path, 'r') as version_file:
            version_number = version_file.readline().rstrip()
    except FileNotFoundError:
        print(version_file_path + ' does not exist')

    return dict(app_version=version_number)





@app.context_processor
def inject_bundle_version():
    """Reads bundle-version.txt to inject bundle_version to Views"""
    version_number = ''

    try:
        with app.open_resource('static/bundle-version.txt', 'r') as version_file:
            version_number = version_file.read()
    except FileNotFoundError:
        print('bundle-version.txt does not exist')

    return dict(bundle_version=version_number)
