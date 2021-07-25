from typing import List

from .abstracts.AbcHighscoreService import AbcHighscoreService

from ..modules.highscore.viewmodels.HighscoreRankViewModel import HighscoreRankViewModel

from ..repositories.HighscoreRankRepository import HighscoreRankRepository


class HighscoreService(AbcHighscoreService):

    @staticmethod
    def get_highscore_rank_viewmodel_list() -> List[HighscoreRankViewModel]:
        """
        Builds all Highscore Ranks and return List of ViewModles
        """

        all_highscoreranks = HighscoreRankRepository.get_all()

        viewmodel_list = []

        for highscorerank in all_highscoreranks:
            viewmodel = HighscoreRankViewModel()
            viewmodel.rank = highscorerank.rank
            viewmodel.user_alias = highscorerank.user_alias
            viewmodel.user_profilepicture = highscorerank.user_profilepicture
            viewmodel.amount_of_games_won = highscorerank.amount_of_games_won

            viewmodel_list.append(viewmodel)

        return viewmodel_list
