from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from datetime import datetime

from .viewmodels.LoginViewModel import LoginViewModel
from .viewmodels.SignupViewModel import SignupViewModel

from ...repositories import UserRepository, UserUserRoleRepository
from ...services import UserService, NotificationService

from ...models.user import User, UserRole, UserUserRole


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

    if request.method == 'POST':

        if login_viewmodel.validate():

            user = UserRepository().find_active_by_email(login_viewmodel.email.data)

            if user and UserService().check_password(user, form.password.data):
                login_user(user)
                return redirect(url_for('home_controller.index'))


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
    signup_viewmodel = SignupViewModel()

    if request.method == 'POST' and signup_viewmodel.validate():

        existing_user = UserRepository().find_by_email(signup_viewmodel.email.data)

        if existing_user is None:

            is_signup_email_validation_inactive = not config['IS_SIGNUP_EMAIL_VALIDATION_ACTIVE']

            new_user = User(
                email=signup_viewmodel.email.data,
                creation_date=datetime.now(),
                is_active=is_signup_email_validation_inactive
            )

            UserService().set_password(new_user, signup_viewmodel.password.data)
            UserRepository().add(new_user)

            user_to_role = UserUserRole(user_id=new_user.id, userrole_id=config['USERROLE_STUDENT'])
            UserUserRoleRepository().add(user_to_role)


            if is_signup_email_validation_inactive:
                login_user(new_user)
                redirect(url_for('home_controller.index'))

            else:
                NotificationService().send_notification(new_user.email, 'Bitte bestätige deine Email-Adresse', '')
                flash('Wir haben dir nun eine Email gesendet. Bitte bestätige deine Emailadresse durch einen Klick auf den Link in der Mail.')
                redirect(url_for('auth_controller.login'))


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