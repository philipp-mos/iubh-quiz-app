from typing import List

from .abstracts.AbcHighscoreService import AbcHighscoreService

from ..models.highscore.HighscoreRank import HighscoreRank
from ..models.user.User import User

from ..modules.highscore.viewmodels.HighscoreRankViewModel import HighscoreRankViewModel

from ..repositories.HighscoreRankRepository import HighscoreRankRepository
from ..repositories.QuizGameResultRepository import QuizGameResultRepository
from ..repositories.UserRepository import UserRepository

from ..helpers.ImageHelper import ImageHelper


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

    @staticmethod
    def calculate_highscores_and_update() -> bool:
        grouped_results = QuizGameResultRepository.get_all_grouped_and_count_by_user()

        highscorerank_list = []

        counter = 0

        for result in grouped_results:

            user: User = UserRepository.find_by_id(result.user_id)

            if not user or not user.is_highscore_enabled:
                continue

            counter += 1

            highscore_rank: HighscoreRank = HighscoreRank()

            highscore_rank.rank = counter
            highscore_rank.user_id = user.id
            highscore_rank.user_alias = user.highscore_alias
            highscore_rank.user_profilepicture = ImageHelper.build_gavatar_image_url(user.email)
            highscore_rank.amount_of_games_won = result.amount_of_games_won

            highscorerank_list.append(highscore_rank)

        return True
