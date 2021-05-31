from .. import login_manager
from flask import redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from .abstracts.AbcUserService import AbcUserService

class UserService(AbcUserService):

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)


    @login_manager.unauthorized_handler
    def unauthorized():
        flash('Bitte melde dich an, um die Seite aufzurufen')
        return redirect(url_for('auth_controller.login'))


    def check_password(User, password):
        return check_password_hash(User.password, password)
