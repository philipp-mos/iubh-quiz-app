from flask import current_app as app
from flask import session
from flask_login import current_user

from os import path

from ..helpers.ImageHelper import ImageHelper

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
            version_number = cache_manager.set_by_key(cache_manager._APPVERSION, version_file.read(), cache_manager._ONEDAY)
    except FileNotFoundError:
        app.logger.error('version.txt does not exist')

    return dict(app_version=version_number)


@app.context_processor
def inject_bundle_version():
    """Reads bundle-version.txt to inject bundle_version to Views"""
    version_number = cache_manager.get_from_key(cache_manager._BUNDLEVERSION)

    if version_number:
        return dict(bundle_version=version_number)

    try:
        with app.open_resource('static/bundle/bundle-version.txt', 'r') as version_file:
            version_number = cache_manager.set_by_key(
                cache_manager._BUNDLEVERSION,
                version_file.read(),
                cache_manager._ONEDAY
            )
    except FileNotFoundError:
        app.logger.error('bundle-version.txt does not exist')

    return dict(bundle_version=version_number)


@app.context_processor
def inject_gravatar_url():
    """
    Build Gravatar Requets Url and provide it to Views
    """
    if not current_user.is_authenticated:
        return dict(user_image='')

    if session.get('USER_IMAGE'):
        return dict(user_image=session['USER_IMAGE'])

    session['USER_IMAGE'] = ImageHelper.build_gavatar_image_url(current_user.email)

    return dict(user_image=session.get('USER_IMAGE'))
