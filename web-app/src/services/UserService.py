import json
from .. import login_manager
from flask import current_app as app
from flask import redirect, url_for, flash, request
from requests import post
from werkzeug.security import generate_password_hash, check_password_hash

from ..repositories.UserRepository import UserRepository

from .abstracts.AbcUserService import AbcUserService

class UserService(AbcUserService):

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return UserRepository().find_by_id(user_id)


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
        User.password = generate_password_hash(password)


    @staticmethod
    def verify_recaptcha(captcha_response, user_remote_ip):

        if not app.config['IS_GOOGLE_RECAPTCHA_ACTIVE']:
            return True

        request_payload = {
            'response': captcha_response, 
            'secret': app.config['GOOGLE_RECAPTCHA_SECRETKEY'],
            'remoteip': user_remote_ip
        }
       
        request_response = post(app.config['GOOGLE_RECAPTCHA_SITEVERIFY_URL'], data=request_payload)

        response_data = json.loads(request_response.text)

        return response_data['success']