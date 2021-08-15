from flask import Blueprint, render_template, session
from flask_login import login_required

from ...services.abstracts.AbcUserService import AbcUserService
from ...services.UserService import UserService
from ...services.abstracts.AbcQuizSuggestionService import AbcQuizSuggestionService
from ...services.QuizSuggestionService import QuizSuggestionService


__quizsuggestionservice: AbcQuizSuggestionService = QuizSuggestionService()
__userservice: AbcUserService = UserService()


tutor_controller = Blueprint(
    'tutor_controller',
    __name__,
    template_folder='views',
    url_prefix='/tutor'
)


@tutor_controller.before_request
@login_required
def before_request():
    # TODO: Move to global Decorator
    if not session.get('USER_IS_TUTOR'):
        return __userservice.unauthorized()


# Tutor/Overview
@tutor_controller.route('/overview', methods=['GET'])
def overview():
    """
    Tutor Quiz-Suggestions Overview
    """

    return render_template(
        'tutor-overview.jinja2',
        viewmodel_list=__quizsuggestionservice.build_tutor_suggestion_overview_viewmodellist()
    )
