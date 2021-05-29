from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_user, login_required, logout_user

from .viewmodels.LoginViewModel import LoginViewModel
from ...repositories.UserRepository import UserRepository
from ...services.UserService import UserService

from ...models.User import User


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

    if request.method == 'POST' and login_viewmodel.validate():

        user = UserRepository().find_by_email(login_viewmodel.email.data)

        if user and UserService().check_password(user, form.password.data):
            login_user(user)
            return redirect(url_for('home_controller.index'))


    return render_template(
        'login.jinja2',
        form=login_viewmodel
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