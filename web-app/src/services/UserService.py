from .. import login_manager
from flask import current_app as app
from flask import redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from .abstracts.AbcUserService import AbcUserService

class UserService(AbcUserService):

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)


    @staticmethod
    @login_manager.unauthorized_handler
    def unauthorized():
        flash('Bitte melde dich an, um die Seite aufzurufen')
        app.logger.info('This Route needs Authentication')
        return redirect(url_for('auth_controller.login'))


    @staticmethod
    def check_password(User, password):
        return check_password_hash(User.password, password)


    @staticmethod
    def set_password(User, password):
        User.password = generate_password_hash(
            password,
            method='sha256'
        )
