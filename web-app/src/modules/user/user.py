from flask import Blueprint, render_template, url_for, escape
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from ...models.user.User import User

from ...repositories.abstracts.AbcUserRepository import AbcUserRepository
from ...repositories.abstracts.AbcQuizGameResultRepository import AbcQuizGameResultRepository
from ...repositories.UserRepository import UserRepository
from ...repositories.QuizGameResultRepository import QuizGameResultRepository


from ...services.abstracts.AbcUserService import AbcUserService
from ...services.abstracts.AbcQuizSuggestionService import AbcQuizSuggestionService
from ...services.UserService import UserService
from ...services.QuizSuggestionService import QuizSuggestionService

from .viewmodels.UserProfileViewModel import UserProfileViewModel

__userrepository: AbcUserRepository = UserRepository()
__quizgameresultrepository: AbcQuizGameResultRepository = QuizGameResultRepository()
__userservice: AbcUserService = UserService()
__quizsuggestionservice: AbcQuizSuggestionService = QuizSuggestionService()


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


# User/Profile
@user_controller.route('/profile', methods=['GET'])
def profile():
    """
    User Profile Overview Page
    """

    user: User = __userrepository.find_by_id(current_user.id)

    role_status = '-'

    if __userservice.is_user_tutor(user):
        role_status = 'Tutor'
    elif __userservice.is_user_student(user):
        role_status = 'Student'

    viewmodel = UserProfileViewModel()
    viewmodel.email = user.email
    viewmodel.is_email_verified = user.is_active
    viewmodel.amount_played_games = __quizgameresultrepository.count_by_user_id(current_user.id)
    viewmodel.is_highscore_enabled.data = user.is_highscore_enabled
    viewmodel.highscore_alias.data = user.highscore_alias
    viewmodel.highscore_rank = 0
    viewmodel.registered_since = user.creation_date.strftime("%d.%m.%Y")
    viewmodel.role_status = role_status
    viewmodel.user_profile_quiz_suggestion = __quizsuggestionservice.get_stat_values_for_user_profile_by_user_id(user.id)

    return render_template(
        'profile.jinja2',
        viewmodel=viewmodel
    )


@user_controller.route('/save-highscore', methods=['POST'])
def save_highscore():
    """
    Saves the User Highscore Setting
    """
    viewmodel = UserProfileViewModel()

    if viewmodel.validate_on_submit():
        user: User = UserRepository.find_by_id(current_user.get_id())
        if not user.is_highscore_enabled:
            user.is_highscore_enabled = viewmodel.is_highscore_enabled.data

        user.highscore_alias = escape(viewmodel.highscore_alias.data)

        UserRepository.commit()

    return redirect(url_for('user_controller.profile'))
