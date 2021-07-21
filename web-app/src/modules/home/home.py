from flask import Blueprint, render_template
from flask_login import login_required

from .viewmodels.DashboardViewModel import DashboardViewModel


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

    return render_template(
        'index.jinja2',
        viewmodel=viewmodel
    )
