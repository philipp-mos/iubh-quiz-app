from abc import ABC, abstractmethod
from typing import List

from ...modules.highscore.viewmodels.HighscoreRankViewModel import HighscoreRankViewModel


class AbcHighscoreService(ABC):

    @abstractmethod
    def get_highscore_rank_viewmodel_list() -> List[HighscoreRankViewModel]:
        raise NotImplementedError

    @abstractmethod
    def calculate_highscores_and_update() -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_last_update_datestring() -> str:
        raise NotImplementedError
