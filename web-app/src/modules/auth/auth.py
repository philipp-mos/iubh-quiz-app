from flask import current_app as app
from flask import Blueprint, render_template, redirect, request, url_for, flash, escape
from flask_login import current_user, login_user, login_required, logout_user
from datetime import datetime

from .viewmodels.LoginViewModel import LoginViewModel
from .viewmodels.SignupViewModel import SignupViewModel

from ...repositories.abstracts.AbcUserRepository import AbcUserRepository
from ...repositories.abstracts.AbcUserUserRoleRepository import AbcUserUserRoleRepository
from ...repositories.UserRepository import UserRepository
from ...repositories.UserUserRoleRepository import UserUserRoleRepository

from ...services.abstracts.AbcUserService import AbcUserService
from ...services.abstracts.AbcNotificationService import AbcNotificationService
from ...services.UserService import UserService
from ...services.NotificationService import NotificationService

from ...models.user.User import User
from ...models.user.UserUserRole import UserUserRole

__userrepository: AbcUserRepository = UserRepository()
__useruserrolerepository: AbcUserUserRoleRepository = UserUserRoleRepository()

__userservice: AbcUserService = UserService()
__notificationservice: AbcNotificationService = NotificationService()


auth_controller = Blueprint(
    'auth_controller',
    __name__,
    template_folder='views',
    url_prefix='/auth'
)


# Auth/Login
@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login View to handle logins via Form
    """

    if current_user.is_authenticated:
        return redirect(url_for('home_controller.index'))

    login_viewmodel = LoginViewModel()

    if request.method == 'POST' and login_viewmodel.validate_on_submit():

        user = __userrepository.find_active_by_email(escape(login_viewmodel.email.data))

        if user and __userservice.check_password(user, login_viewmodel.password.data):
            login_user(user)

            return redirect(url_for(request.args.get('redirect_url') or 'home_controller.index'))

        flash('Email-Adresse oder Passwort ungültig')
        return redirect(url_for('auth_controller.login'))

    return render_template(
        'login.jinja2',
        form=login_viewmodel
    )


# Auth/Signup
@auth_controller.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Creates new Users if valid data was sent
    """

    if current_user.is_authenticated:
        return redirect(url_for('home_controller.index'))

    signup_viewmodel = SignupViewModel()

    if request.method == 'POST' and signup_viewmodel.validate_on_submit():

        existing_user = __userrepository.find_by_email(escape(signup_viewmodel.email.data))

        if existing_user is None:

            if not __userservice.verify_recaptcha(request.form['recaptcha-token'], request.remote_addr):
                flash('Das hat leider nicht geklappt.')
                return redirect(url_for('auth_controller.signup'))

            if not signup_viewmodel.email.data.endswith(app.config['USER_SIGNUP_EMAIL_LIMITATION']):
                flash('Diese Email Adresse ist nicht erlaubt')
                app.logger.info('Email-Domain is not allowed')
                return render_template(
                    'signup.jinja2',
                    form=signup_viewmodel
                )

            is_signup_email_validation_active = app.config['IS_SIGNUP_EMAIL_VALIDATION_ACTIVE']

            new_user = User(
                email=escape(signup_viewmodel.email.data),
                creation_date=datetime.now(),
                is_active=not is_signup_email_validation_active
            )

            __userservice.set_password(new_user, signup_viewmodel.password.data)
            __userrepository.add_and_commit(new_user)

            user_to_role = UserUserRole(user_id=new_user.id, userrole_id=app.config['USERROLE_STUDENT'])
            __useruserrolerepository.add_and_commit(user_to_role)

            if not is_signup_email_validation_active:
                login_user(new_user)
                return redirect(url_for('home_controller.index'))

            else:
                __notificationservice.send_notification(new_user.email, 'Bitte bestätige deine Email-Adresse', '')
                flash(
                    'Wir haben dir nun eine Email gesendet. '
                    'Bitte bestätige deine Emailadresse durch einen Klick auf den Link in der Mail.'
                )
                return redirect(url_for('auth_controller.login'))

        flash('Du bist bereits registriert')

    return render_template(
        'signup.jinja2',
        form=signup_viewmodel
    )


# Auth/Forgot-Password
@auth_controller.route('/forgot-password', methods=['GET'])
def forgot_password():
    return render_template('forgot-password.jinja2')


# Auth/Logout
@auth_controller.route('/logout', methods=['GET'])
@login_required
def logout():
    """
    Logout Action
    """

    logout_user()

    return redirect(url_for('auth_controller.login'))
