from flask import Blueprint
from flask import render_template
from flask_login import current_user

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

    if current_user.is_authenticated:
        return redirect(url_for('home_controller.index'))

    login_viewmodel = LoginViewModel()

    if request.method == 'POST' and login_viewmodel.validate():
        user = UserRepository().find_by_email(login_viewmodel.email.data)

        if user and UserService().check_password(user, form.password.data):
            login_user(user)

           

    return render_template(
        'login.jinja2',
        form=login_viewmodel
    )
