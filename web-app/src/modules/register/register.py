from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_user, login_required, logout_user

from .viewmodels.RegisterViewModel import RegisterViewModel
from ...repositories.UserRepository import UserRepository
from ...services.UserService import UserService

from ...models.user.User import User


register_controller = Blueprint(
    'register',
    __name__,
    template_folder='views',
    url_prefix='/register'
)


## register/new ##
@register_controller.route('/new', methods=['GET', 'POST'])
def register():
    """
    Register View to handle Registrations via Form
    """

    if current_user.is_authenticated:
        return redirect(url_for('home_controller.index'))

    register_viewmodel = RegisterViewModel()

    if request.method == 'POST' and register_viewmodel.validate():

        user = UserRepository().find_by_email(register_viewmodel.email.data)

        if user and UserService().check_password(user, form.password.data):
            register_user(user)
            return redirect(url_for('home_controller.index'))


    return render_template(
        'register.jinja2',
        form=register_viewmodel
    )



