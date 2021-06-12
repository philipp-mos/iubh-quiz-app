from flask import current_app as app
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from datetime import datetime

from .viewmodels.LoginViewModel import LoginViewModel
from .viewmodels.SignupViewModel import SignupViewModel

from ...repositories.UserRepository import UserRepository
from ...repositories.UserUserRoleRepository import UserUserRoleRepository

from ...services.UserService import UserService
from ...services.NotificationService import NotificationService

from ...models.user.User import User
from ...models.user.UserRole import UserRole
from ...models.user.UserUserRole import UserUserRole


auth_controller = Blueprint(
    'auth_controller',
    __name__,
    template_folder='views',
    url_prefix='/auth'
)


## Auth/Login ##
@auth_controller.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login View to handle logins via Form
    """

    if current_user.is_authenticated:
        return redirect(url_for('home_controller.index'))

    login_viewmodel = LoginViewModel()

    if request.method == 'POST' and login_viewmodel.validate_on_submit():

        user = UserRepository().find_active_by_email(login_viewmodel.email.data)

        if user and UserService().check_password(user, login_viewmodel.password.data):
            login_user(user)

            return redirect(url_for(request.args.get('redirect_url') or 'home_controller.index'))


        flash('Email-Adresse oder Passwort ungültig')
        return redirect(url_for('auth_controller.login'))


    return render_template(
        'login.jinja2',
        form=login_viewmodel
    )


## Auth/Signup ##
@auth_controller.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Creates new Users if valid data was sent
    """

    if current_user.is_authenticated:
        return redirect(url_for('home_controller.index'))


    signup_viewmodel = SignupViewModel()

    if request.method == 'POST' and signup_viewmodel.validate_on_submit():

        existing_user = UserRepository().find_by_email(signup_viewmodel.email.data)

        if existing_user is None:

            if not UserService().verify_recaptcha(request.form['recaptcha-token'], request.remote_addr):
                flash('Das hat leider nicht geklappt.')
                return redirect(url_for('auth_controller.signup'))


            if not signup_viewmodel.email.data.endswith(app.config['USER_SIGNUP_EMAIL_LIMITATION']):
                flash('Diese Email Adresse ist nicht erlaubt')
                app.logger.info('Email-Domain is not allowed')
                return render_template(
                    'signup.jinja2',
                    form=signup_viewmodel
                )

            is_signup_email_validation_inactive = not app.config['IS_SIGNUP_EMAIL_VALIDATION_ACTIVE']

            new_user = User(
                email=signup_viewmodel.email.data,
                creation_date=datetime.now(),
                is_active=is_signup_email_validation_inactive
            )

            UserService().set_password(new_user, signup_viewmodel.password.data)
            UserRepository().add_and_commit(new_user)

            user_to_role = UserUserRole(user_id=new_user.id, userrole_id=app.config['USERROLE_STUDENT'])
            UserUserRoleRepository().add_and_commit(user_to_role)


            if is_signup_email_validation_inactive:
                login_user(new_user)
                return redirect(url_for('home_controller.index'))

            else:
                NotificationService().send_notification(new_user.email, 'Bitte bestätige deine Email-Adresse', '')
                flash('Wir haben dir nun eine Email gesendet. Bitte bestätige deine Emailadresse durch einen Klick auf den Link in der Mail.')
                return redirect(url_for('auth_controller.login'))


        flash('Du bist bereits registriert')
    
    return render_template(
        'signup.jinja2',
        form=signup_viewmodel
    )


## Auth/Logout ##
@auth_controller.route('/logout', methods=['GET'])
@login_required
def logout():
    """
    Logout Action
    """

    logout_user()

    return redirect(url_for('auth_controller.login'))
