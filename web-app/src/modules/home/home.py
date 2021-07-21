from flask import current_app as app
from flask import Blueprint, render_template
from flask_login import login_required

from .viewmodels.DashboardViewModel import DashboardViewModel

from ...services.QuizService import QuizService

from ...repositories.SubjectRepository import SubjectRepository


home_controller = Blueprint(
    'home_controller',
    __name__,
    template_folder='views',
    url_prefix=''
)


@home_controller.before_request
@login_required
def before_request():
    pass


# Home/Index
@home_controller.route('/', methods=['GET'])
def index():
    """
    User Dashboard
    """
    viewmodel = DashboardViewModel()
    viewmodel.random_quiz_id = 0

    random_subject = SubjectRepository.get_random_item()

    if random_subject:
        viewmodel.random_quiz_id = random_subject.id

    viewmodel.dashboard_game_list_items = QuizService.get_played_games_for_quiz_game_overview(
        app.config.get('DASHBOARD_AMOUNT_OF_QUIZGAMES')
    )

    return render_template(
        'index.jinja2',
        viewmodel=viewmodel
    )
