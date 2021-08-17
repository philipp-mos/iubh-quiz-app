from flask import Blueprint, render_template, session, redirect, url_for
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


# Tutor/Detail
@tutor_controller.route('/detail/<int:suggest_number>', methods=['GET'])
def detail(suggest_number: int):
    """
    Tutor Quiz-Suggestions Detail Page
    """

    if __quizsuggestionservice.is_invalid_suggestion_id(suggest_number):
        return redirect(url_for('tutor_controller.overview'))

    return render_template(
        'tutor-detail.jinja2',
        viewmodel=__quizsuggestionservice.build_tutor_detail_viewmodel(suggest_number)
    )
