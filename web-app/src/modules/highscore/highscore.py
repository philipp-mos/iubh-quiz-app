from flask import Blueprint, render_template
from flask_login import login_required

from ...services.abstracts.AbcHighscoreService import AbcHighscoreService
from ...services.HighscoreService import HighscoreService


__highscoreservice: AbcHighscoreService = HighscoreService()


highscore_controller = Blueprint(
    'highscore_controller',
    __name__,
    template_folder='views',
    url_prefix='/highscore'
)


@highscore_controller.before_request
@login_required
def before_request():
    pass


# Highscore/Overview
@highscore_controller.route('/overview', methods=['GET'])
def overview():
    """
    Highscore-Übersicht
    """

    return render_template(
        'highscore.jinja2',
        viewmodel=__highscoreservice.get_highscore_rank_viewmodel_list()
    )
