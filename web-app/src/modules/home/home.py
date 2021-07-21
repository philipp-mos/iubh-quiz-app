import datetime

from flask import Blueprint, render_template
from flask_login import login_required

from .viewmodels.DashboardViewModel import DashboardViewModel
from .viewmodels.DashboardGameListItemViewModel import DashboardGameListItemViewModel

from ...services.QuizService import QuizService


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

    viewmodel.random_quiz_id = 8
    viewmodel.dashboard_game_list_items = []

    all_quizgames = QuizService.get_played_games_for_dashboard()

    for quizgame in all_quizgames:
        game_listitem = DashboardGameListItemViewModel()
        game_listitem.id = quizgame.id
        game_listitem.date = quizgame.creation_date.strftime('%d.%m.%Y %H:%M')

        viewmodel.dashboard_game_list_items.append(game_listitem)

    return render_template(
        'index.jinja2',
        viewmodel=viewmodel
    )
