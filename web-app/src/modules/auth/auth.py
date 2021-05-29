from flask import Blueprint
from flask import render_template
from flask_login import current_user

from .viewmodels.LoginViewModel import LoginViewModel

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

    return render_template(
        'login.jinja2',
        form=LoginViewModel()
    )
