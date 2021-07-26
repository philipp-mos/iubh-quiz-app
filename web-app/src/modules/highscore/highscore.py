from flask import Blueprint, render_template
from flask_login import login_required

from ... import cache_manager

from .viewmodels.HighscoreOverviewViewModel import HighscoreOverviewViewModel

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
    viewmodel: HighscoreOverviewViewModel = cache_manager.get_from_key(cache_manager._HIGHSCOREOVERVIEWVIEWMODEL)

    if not viewmodel:
        viewmodel = cache_manager.set_by_key(
            cache_manager._HIGHSCOREOVERVIEWVIEWMODEL,
            __highscoreservice.get_highscoreoverview_viewmodel(),
            cache_manager._ONEHOUR
        )

    return render_template(
        'highscore.jinja2',
        viewmodel=viewmodel
    )
