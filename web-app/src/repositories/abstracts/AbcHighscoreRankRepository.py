from abc import abstractmethod
from .AbcRepository import AbcRepository

from ...models.highscore.HighscoreRank import HighscoreRank


class AbcHighscoreRankRepository(AbcRepository):

    @abstractmethod
    def find_by_rank(rank: int) -> HighscoreRank:
        raise NotImplementedError
