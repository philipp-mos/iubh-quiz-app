from flask import current_app as app


@app.context_processor
def inject_bundle_version():

    version_number = ''

    try:
        with app.open_resource('static/bundle-version.txt', 'r') as version_file:
            version_number = version_file.read()
    except FileNotFoundError:
        print('bundle-version.txt does not exist')

    return dict(bundle_version=version_number)