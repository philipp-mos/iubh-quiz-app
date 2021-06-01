from .. import login_manager
from flask import redirect, url_for
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
        return redirect(url_for('auth_controller.login'))


    @staticmethod
    def check_password(User, password):
        return check_password_hash(User.password, password)
