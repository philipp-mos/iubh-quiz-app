from abc import ABC, abstractmethod
from typing import List

from ...modules.highscore.viewmodels.HighscoreRankViewModel import HighscoreRankViewModel


class AbcHighscoreService(ABC):

    @abstractmethod
    def get_highscore_rank_viewmodel_list() -> List[HighscoreRankViewModel]:
        raise NotImplementedError
