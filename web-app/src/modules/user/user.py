from flask import Blueprint, render_template
from flask_login import login_required, current_user

from ...repositories.UserRepository import UserRepository

from ...services.UserService import UserService
from ...services.QuizSuggestionService import QuizSuggestionService

from .viewmodels.UserProfileViewModel import UserProfileViewModel
from .viewmodels.UserProfileQuizSuggestionViewModel import UserProfileQuizSuggestionViewModel


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
    
    role_status = '-'

    if UserService.is_user_tutor(user):
        role_status = 'Tutor'
    elif UserService.is_user_student(user):
        role_status = 'Student'


    return render_template(
        'profile.jinja2',
        viewmodel=UserProfileViewModel(
            user.email,
            user.is_active,
            user.creation_date.strftime("%d.%m.%Y"),
            role_status,
            user_profile_quiz_suggestion=QuizSuggestionService().get_stat_values_for_user_profile_by_user_id(user.id)
        )
    )
