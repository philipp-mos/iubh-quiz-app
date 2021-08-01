from flask import Blueprint, jsonify
from flask_login import login_required, current_user

from .dtos.DashboardHistoricQuizResultsDto import DashboardHistoricQuizResultsDto

from ...repositories.abstracts.AbcQuizGameResultRepository import AbcQuizGameResultRepository
from ...repositories.QuizGameResultRepository import QuizGameResultRepository


__quizgameresultrepository: AbcQuizGameResultRepository = QuizGameResultRepository()


api_v1__quizgameresult_controller = Blueprint(
    'api_v1__quizgameresult_controller',
    __name__,
    url_prefix='/api/v1/quizgameresult'
)


@api_v1__quizgameresult_controller.before_request
@login_required
def before_request():
    pass


@api_v1__quizgameresult_controller.route('/gethistoric-ytd', methods=['GET'])
def get_historic_ytd():
    """
    Get Historic Data of games Won YTD
    """

    quizgameresults = __quizgameresultrepository.get_quizgameresults_by_userid(current_user.get_id())

    historicresults_dto = DashboardHistoricQuizResultsDto()

    for quizgameresult in quizgameresults:
        monthselection: int = quizgameresult.creation_date.month - 1

        if quizgameresult.is_won:
            historicresults_dto.won[monthselection] += 1
        else:
            historicresults_dto.lost[monthselection] += 1

    return jsonify(historicresults_dto.to_json()), 200
