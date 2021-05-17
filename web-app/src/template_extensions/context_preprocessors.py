from flask import current_app as app


@app.context_processor
def inject_bundle_version():

    with app.open_resource('static/bundle-version.txt', 'r') as version_file:
        version_number = version_file.read()

    return dict(bundle_version=version_number)