from flask import Blueprint, render_template
from flask_login import login_required, current_user

from ...repositories.UserRepository import UserRepository

from ...services.UserService import UserService

from .viewmodels.UserProfileViewModel import UserProfileViewModel


user_controller = Blueprint(
    'user_controller',
    __name__,
    template_folder='views',
    url_prefix='/user'
)


@user_controller.before_request
@login_required
def before_request():
    pass



## User/Profile ##
@user_controller.route('/profile', methods=['GET'])
def profile():
    """
    User Profile Overview Page
    """

    user = UserRepository().find_by_id(current_user.id)
    
    user_status = '-'

    if UserService.is_user_tutor(user):
        user_status = 'Tutor'
    elif UserService.is_user_student(user):
        user_status = 'Student'


    return render_template(
        'profile.jinja2',
        viewmodel=UserProfileViewModel(
            user.email,
            user.creation_date.strftime("%d.%m.%Y"),
            user_status
        )
    )
